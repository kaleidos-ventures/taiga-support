from setuptools import setup

setup(
    name='lektor-makdown-image-absolute-links',
    version='0.1',
    author=u'David Barrag\xe1n',
    author_email='bameda@dbarragan.com',
    license='MIT',
    py_modules=['lektor_makdown_image_absolute_links'],
    entry_points={
        'lektor.plugins': [
            'makdown-image-absolute-links = lektor_makdown_image_absolute_links:MakdownImageAbsoluteLinksPlugin',
        ]
    }
)
