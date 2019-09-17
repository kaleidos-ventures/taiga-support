import os
import sys
import uuid
import errno
import tempfile

from collections import MutableMapping, OrderedDict


PY2 = sys.version_info[0] == 2
WIN = sys.platform.startswith('win')


if PY2:
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)
    iteritems = lambda x: x.iteritems()
    exec('def reraise(tp, value, tb=None):\n raise tp, value, tb')
else:
    text_type = str
    string_types = (str,)
    integer_types = (int,)
    iteritems = lambda x: iter(x.items())
    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value


def _posixify(name):
    return '-'.join(name.split()).lower()


def iter_from_file(f, encoding=None):
    if encoding is None:
        encoding = 'utf-8-sig'
    return (x.decode(encoding, 'replace') for x in f)


def get_app_dir(app_name, roaming=True, force_posix=False):
    r"""Returns the config folder for the application.  The default behavior
    is to return whatever is most appropriate for the operating system.

    To give you an idea, for an app called ``"Foo Bar"``, something like
    the following folders could be returned:

    Mac OS X:
      ``~/Library/Application Support/Foo Bar``
    Mac OS X (POSIX):
      ``~/.foo-bar``
    Unix:
      ``~/.config/foo-bar``
    Unix (POSIX):
      ``~/.foo-bar``
    Win XP (roaming):
      ``C:\Documents and Settings\<user>\Local Settings\Application Data\Foo Bar``
    Win XP (not roaming):
      ``C:\Documents and Settings\<user>\Application Data\Foo Bar``
    Win 7 (roaming):
      ``C:\Users\<user>\AppData\Roaming\Foo Bar``
    Win 7 (not roaming):
      ``C:\Users\<user>\AppData\Local\Foo Bar``

    :param app_name: the application name.  This should be properly capitalized
                     and can contain whitespace.
    :param roaming: controls if the folder should be roaming or not on Windows.
                    Has no affect otherwise.
    :param force_posix: if this is set to `True` then on any POSIX system the
                        folder will be stored in the home folder with a leading
                        dot instead of the XDG config home or darwin's
                        application support folder.
    """
    if WIN:
        key = roaming and 'APPDATA' or 'LOCALAPPDATA'
        folder = os.environ.get(key)
        if folder is None:
            folder = os.path.expanduser('~')
        return os.path.join(folder, app_name)
    if force_posix:
        return os.path.join(os.path.expanduser('~/.' + _posixify(app_name)))
    if sys.platform == 'darwin':
        return os.path.join(os.path.expanduser(
            '~/Library/Application Support'), app_name)
    return os.path.join(
        os.environ.get('XDG_CONFIG_HOME', os.path.expanduser('~/.config')),
        _posixify(app_name))


class Dialect(object):
    """This class allows customizing the dialect of the ini file.  The
    default configuration is a compromise between the general Windows
    format and what's common on Unix systems.

    Example dialect config::

        unix_dialect = Dialect(
            kv_sep=': ',
            quotes=("'",),
            comments=('#',),
        )

    :param ns_sep: the namespace separator.  This character is used to
                   create hierarchical structures in sections and also
                   placed between section and field.
    :param kv_sep: the separator to be placed between key and value.  For
                   parsing whitespace is automatically removed.
    :param quotes: a list of quote characters supported for strings.  The
                   leftmost one is automatically used for serialization,
                   the others are supported for deserialization.
    :param true: strings that should be considered boolean true.
    :param false: strings that should be considered boolean false.
    :param comments: comment start markers.
    :param allow_escaping: enables or disables backslash escapes.
    :param linesep: a specific line separator to use other than the
                    operating system's default.
    """

    def __init__(self, ns_sep='.', kv_sep=' = ', quotes=('"', "'"),
                 true=('true', 'yes', '1'), false=('false', 'no', '0'),
                 comments=('#', ';'), allow_escaping=True, linesep=None):
        self.ns_sep = ns_sep
        self.kv_sep = kv_sep
        self.plain_kv_sep = kv_sep.strip()
        self.quotes = quotes
        self.true = true
        self.false = false
        self.comments = comments
        self.allow_escaping = allow_escaping
        self.linesep = linesep

    def get_actual_linesep(self):
        if self.linesep is None:
            return os.linesep
        return self.linesep

    def get_strippable_lineseps(self):
        if self.linesep is None or self.linesep in '\r\n':
            return '\r\n'
        return self.linesep

    def kv_serialize(self, key, val):
        if val is None:
            return None
        if self.quotes and val.split() != [val]:
            q = self.quotes[0]
            if self.allow_escaping:
                val = self.escape(val, q)
            val = '%s%s%s' % (q, val, q)
        return '%s%s%s' % (key, self.kv_sep, val)

    def escape(self, value, quote=None):
        value = value \
            .replace('\\', '\\\\') \
            .replace('\n', '\\n') \
            .replace('\r', '\\r') \
            .replace('\t', '\\t')
        for q in self.quotes:
            if q != quote:
                value = value.replace(q, '\\' + q)
        return value

    def unescape(self, value):
        value = value \
            .replace('\\n', '\n') \
            .replace('\\r', '\r') \
            .replace('\\t', '\t') \
            .replace('\\"', '"')
        for q in self.quotes:
            value = value.replace('\\' + q, q)
        return value

    def to_string(self, value):
        if value is True:
            return self.true[0]
        if value is False:
            return self.false[0]
        if isinstance(value, integer_types) or isinstance(value, float):
            return text_type(value)
        if not isinstance(value, string_types):
            raise TypeError('Cannot set value of this type')
        return text_type(value)

    def dict_from_iterable(self, iterable):
        """Builds a mapping of values out of an iterable of lines."""
        mapping = OrderedDict()
        for token, _, data in self.tokenize(iterable):
            if token == 'KV':
                section, key, value = data
                mapping[self.ns_sep.join(section + (key,))] = value
        return mapping

    def tokenize(self, iterable):
        """Tokenizes an iterable of lines."""
        section = ()

        line_strip = self.get_strippable_lineseps()

        for line in iterable:
            line = line.rstrip(line_strip)
            if not line.strip():
                yield 'EMPTY', line, None
            elif line.lstrip()[:1] in self.comments:
                yield 'COMMENT', line, None
            elif line[:1] == '[' and line[-1:] == ']':
                section = tuple(line[1:-1].strip().split(self.ns_sep))
                yield 'SECTION', line, section
            elif self.plain_kv_sep in line:
                key, value = line.split(self.plain_kv_sep, 1)
                value = value.strip()
                if value[:1] in self.quotes and value[:1] == value[-1:]:
                    value = value[1:-1]
                    if self.allow_escaping:
                        value = self.unescape(value)
                yield 'KV', line, (section, key.strip(), value)

    def update_tokens(self, old_tokens, changes):
        """Given the tokens returned from :meth:`tokenize` and a dictionary
        of new values (or `None` for values to be deleted) returns a new
        list of tokens that should be written back to a file.
        """
        new_tokens = []
        section_ends = {None: 0}
        pending_changes = dict(changes)

        for token, line, data in old_tokens:
            if token == 'KV':
                section, key, value = data
                k = self.ns_sep.join(section + (key,))
                if k in pending_changes:
                    value = pending_changes.pop(k)
                    line = self.kv_serialize(key, value)
                    data = (section, key, value)
                section_ends[self.ns_sep.join(section)] = len(new_tokens)
            elif token == 'SECTION':
                section_ends[self.ns_sep.join(data)] = len(new_tokens)
            new_tokens.append((token, line, data))

        pending_by_sec = {}
        for key, value in sorted(pending_changes.items()):
            section, local_key = key.rsplit(self.ns_sep, 1)
            pending_by_sec.setdefault(section, []).append((local_key, value))

        if pending_by_sec:
            section_ends_r = dict((v, k) for k, v in section_ends.items())
            final_lines = []

            for idx, (token, line, data) in enumerate(new_tokens):
                final_lines.append((token, line, data))
                section = section_ends_r.get(idx)
                if section is not None and section in pending_by_sec:
                    for local_key, value in pending_by_sec.pop(section):
                        final_lines.append((
                            'KV',
                            self.kv_serialize(local_key, value),
                            (section, local_key, value),
                        ))

            for section, items in sorted(pending_by_sec.items()):
                if final_lines:
                    final_lines.append(('EMPTY', u'', None))
                final_lines.append(('SECTION', u'[%s]' % section, section))
                for local_key, value in items:
                    final_lines.append((
                        'KV',
                        self.kv_serialize(local_key, value),
                        (section, local_key, value),
                    ))

            new_tokens = final_lines

        return [x for x in new_tokens if x[1] is not None]


default_dialect = Dialect()


class IniData(MutableMapping):
    """This object behaves similar to a dictionary but it tracks
    modifications properly so that it can later write them back to an INI
    file with the help of the ini dialect, without destroying ordering or
    comments.

    This is rarely used directly, instead the :class:`IniFile` is normally
    used.

    This generally works similar to a dictionary and exposes the same
    basic API.
    """

    def __init__(self, mapping=None, dialect=None):
        if dialect is None:
            dialect = default_dialect
        self.dialect = dialect
        if mapping is None:
            mapping = {}
        self._primary = mapping
        self._changes = {}

    @property
    def is_dirty(self):
        """This is true if the data was modified."""
        return bool(self._changes)

    def get_updated_lines(self, line_iter=None):
        """Reconciles the updates in the ini data with the iterator of
        lines from the source file and returns a list of the new lines
        as they should be written into the file.
        """
        return self.dialect.update_tokens(line_iter or (), self._changes)

    def discard(self):
        """Discards all local modifications in the ini data."""
        self._changes.clear()

    def rollover(self):
        """Rolls all local modifications to the primary data.  After this
        modifications are no longer tracked and `get_updated_lines` will
        not return them.
        """
        self._primary = OrderedDict(self.iteritems())
        self.discard()

    def to_dict(self):
        """Returns the current ini data as dictionary."""
        return dict(self.iteritems())

    def __len__(self):
        rv = len(self._primary)
        for key, value in iteritems(self._changes):
            if key in self._primary and value is not None:
                rv += 1
        return rv

    def get(self, name, default=None):
        """Return a value for a key or return a default if the key does
        not exist.
        """
        try:
            return self[name]
        except KeyError:
            return default

    def get_ascii(self, name, default=None):
        """This returns a value for a key for as long as the value fits
        into ASCII.  Otherwise (or if the key does not exist) the default
        is returned.  This is especially useful on Python 2 when working
        with some APIs that do not support unicode.
        """
        try:
            rv = self[name]
            try:
                rv.encode('ascii')
            except UnicodeError:
                raise KeyError()
            if PY2:
                rv = str(rv)
            return rv
        except KeyError:
            return default

    def get_bool(self, name, default=False):
        """Returns a value as boolean.  What constitutes as a valid boolean
        value depends on the dialect.
        """
        try:
            rv = self[name].lower()
            if rv in self.dialect.true:
                return True
            if rv in self.dialect.false:
                return False
            raise KeyError()
        except KeyError:
            return default

    def get_int(self, name, default=None):
        """Returns a value as integer."""
        try:
            return int(self[name])
        except (ValueError, KeyError):
            return default

    def get_float(self, name, default=None):
        """Returns a value as float."""
        try:
            return float(self[name])
        except (ValueError, KeyError):
            return default

    def get_uuid(self, name, default=None):
        """Returns a value as uuid."""
        try:
            return uuid.UUID(self[name])
        except Exception:
            return default

    def itersections(self):
        """Iterates over the sections of the sections of the ini."""
        seen = set()
        sep = self.dialect.ns_sep
        for key in self:
            if sep in key:
                section = key.rsplit(sep, 1)[0]
                if section not in seen:
                    seen.add(section)
                    yield section

    if PY2:
        def sections(self):
            """Returns a list of the sections in the ini file."""
            return list(self.itersections())
    else:
        sections = itersections

    def iteritems(self):
        for key in self._primary:
            try:
                yield key, self[key]
            except LookupError:
                pass
        for key in self._changes:
            if key not in self._primary:
                try:
                    yield key, self[key]
                except LookupError:
                    pass

    def iterkeys(self):
        for key, _ in self.iteritems():
            yield key

    def itervalues(self):
        for _, value in self.iteritems():
            yield value

    __iter__ = iterkeys

    if PY2:
        def keys(self):
            return list(self.iterkeys())

        def values(self):
            return list(self.iterkeys())

        def items(self):
            return list(self.iteritems())
    else:
        keys = iterkeys
        values = itervalues
        items = iteritems

    def section_as_dict(self, section):
        rv = {}
        prefix = section + '.'
        for key, value in self.iteritems():
            if key.startswith(prefix):
                rv[key[len(prefix):]] = value
        return rv

    def __getitem__(self, name):
        if name in self._changes:
            rv = self._changes[name]
            if rv is None:
                raise KeyError(name)
            return rv
        return self._primary[name]

    def __setitem__(self, name, value):
        self._changes[name] = self.dialect.to_string(value)

    def __delitem__(self, name):
        self._changes[name] = None


class IniFile(IniData):
    """This class implements simplified read and write access to INI files
    in a way that preserves the original files as good as possible.  Unlike
    a regular INI serializer it only overwrites the lines that were modified.

    Example usage::

        ifile = IniFile('myfile.ini')
        ifile['ui.username'] = 'john_doe'
        ifile.save()

    The ini file exposes unicode strings but utility methods are provided
    for common type conversion.  The default namespace separator is a dot
    (``.``).

    The format of the file can be configured by providing a custom
    :class:`Dialect` instance to the constructor.
    """

    def __init__(self, filename, encoding=None, dialect=None):
        if dialect is None:
            dialect = default_dialect
        self.filename = os.path.abspath(filename)
        self.encoding = encoding

        try:
            with open(filename, 'rb') as f:
                mapping = dialect.dict_from_iterable(
                        iter_from_file(f, self.encoding))
                is_new = False
        except IOError as e:
            if e.errno != errno.ENOENT:
                raise
            is_new = True
            mapping = OrderedDict()

        IniData.__init__(self, mapping, dialect)

        #: If this is `true` the file did not exist yet (it is new).  This
        #: can be used to fill it with some defaults.
        self.is_new = is_new

    def save(self, create_folder=False):
        """Saves all modifications back to the file.  By default the folder
        in which the file is placed needs to exist.
        """
        # No modifications means no write.
        if not self.is_dirty:
            return

        enc = self.encoding
        if enc is None:
            enc = 'utf-8'
        linesep = self.dialect.get_actual_linesep()

        if create_folder:
            folder = os.path.dirname(self.filename)
            try:
                os.makedirs(folder)
            except OSError:
                pass

        try:
            with open(self.filename, 'rb') as f:
                old_tokens = list(self.dialect.tokenize(
                    iter_from_file(f, self.encoding)))
        except IOError:
            old_tokens = []

        fd, tmp_filename = tempfile.mkstemp(
            dir=os.path.dirname(self.filename), prefix='.__atomic-write')
        try:
            with os.fdopen(fd, 'wb') as f:
                new_tokens = self.get_updated_lines(old_tokens)
                for _, line, _ in new_tokens:
                    f.write((line + linesep).encode(enc))
        except:
            exc_info = sys.exc_info()
            try:
                os.remove(tmp_filename)
            except OSError:
                pass
            reraise(*exc_info)

        if hasattr(os, 'replace'):
            os.replace(tmp_filename, self.filename)
        else:
            try:
                os.rename(tmp_filename, self.filename)
            except OSError:
                if os.name == 'nt':
                    os.remove(self.filename)
                    os.rename(tmp_filename, self.filename)
                else:
                    raise
        self.rollover()
        self.is_new = False


class AppIniFile(IniFile):
    """This works exactly the same as :class:`IniFile` but the ini files
    are placed by default in an application config directory.  This uses
    the function :func:`get_app_dir` internally to calculate the path
    to it.  Also by default the :meth:`~IniFile.save` method will create
    the folder if it did not exist yet.

    Example::

        from inifile import AppIniFile

        config = AppIniFile('My App', 'my_config.ini')
        config['ui.user_colors'] = True
        config['ui.colorscheme'] = 'tango'
        config.save()
    """

    def __init__(self, app_name, filename, roaming=True, force_posix=False,
                 encoding=None, dialect=None):
        app_dir = get_app_dir(app_name, roaming=roaming,
                              force_posix=force_posix)
        IniFile.__init__(self, os.path.join(app_dir, filename),
                         encoding=encoding, dialect=dialect)

    def save(self, create_folder=True):
        return IniFile.save(self, create_folder=create_folder)
