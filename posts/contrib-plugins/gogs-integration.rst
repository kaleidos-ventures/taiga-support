.. title: Gogs integration
.. slug: gogs-integration
.. date: 2015-10-16 13:55:08 UTC+02:00
.. tags: 
.. category: Contrib Plugins
.. order: 10
.. link: 
.. description: 
.. type: text

*Gogs is a self-hosted Git service written in Go.*

First things first, Gogs is a huge platform with lots of features.
Integration will always take time so please be patient. If you need a
specific integration and you feel ready to get your machete and cut
right into the taiga, please review our `API Docs`_.

If you need help with a specific feature, you can always get in touch
with our community through our `mailing list`_.

1. Configure Taiga
~~~~~~~~~~~~~~~~~~

In your project:

1. Go to *Admin > Contrib plugins > Gogs*
   |Taiga Gogs Menu|

2. Fill in the Secret key or use the one that it is auto generated
   |Taiga Gogs Options|

3. Copy the Payload URL field.

2. Configure Gogs
~~~~~~~~~~~~~~~~~

Go to your repository

1. Click on *Settings > Webhooks > Add webhook*

2. On the form set the *Payload URL* and the *Secret* with the payload
   URL and Secret key from Taiga.

3. Taiga only listen for push events (changing element status via commit
    message) in the case of gogs.
   |Gogs Webhooks|

Changing elements status via commit message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The status of any issue, task or user story can be changed via commit
  message. You may want to read more
| `about this feature`_

.. _API Docs: http://taigaio.github.io/taiga-doc/dist/api.html
.. _mailing list: https://groups.google.com/forum/#!forum/taigaio
.. _about this feature: https://taiga.io/support/changing-elements-status-via-commit-message/

.. |Taiga Gogs Menu| image:: /resources/contrib-plugins/gogs-integration//taiga-gogs-menu.png
.. |Taiga Gogs Options| image:: /resources/contrib-plugins/gogs-integration//taiga-gogs-options.png
.. |Gogs Webhooks| image:: /resources/contrib-plugins/gogs-integration//gogs-webhooks.png
