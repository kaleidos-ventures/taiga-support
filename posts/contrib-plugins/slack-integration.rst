.. title: Slack integration
.. slug: slack-integration
.. date: 2015-10-16 13:55:09 UTC+02:00
.. tags: 
.. category: Contrib Plugins
.. order: 30
.. link: 
.. description: 
.. type: text


*Slack is a platform for team communication.*

First things first, Slack is a huge platform with lots of features.
Integration will always take time so please be patient. If you need a
specific integration and you feel ready to get out your machete and
start cutting into the taiga, please review our `API Docs`_.

If you need help with a specific feature, you can always get in touch
with our community through our `mailing list`_.

1. Configure Slack
~~~~~~~~~~~~~~~~~~

Go to your slack app

1. Go to *Configure Integrations*. |Slack Integration Step 1|

2. Add a new “Incoming WebHooks” integration. |Slack Integration Step 2|

3. Choose a channel and click *Add Incoming WebHooks Integration*.
   |Slack Integration Step 3|

4. Copy your *Webhook URL*. |Slack Integration Step 4|

2. Configure Taiga
~~~~~~~~~~~~~~~~~~

In Taiga:

1. Go to *Admin > Plugins > Slack*
   |Taiga Admin Slack Menu|

2. Set the *Slack webhook url* to the copied value in the previous step.

3. You can also set the Slack channel which your project will post to.
   Leave the field blank if you wish to post to the default channel.
   |Taiga Admin Slack Options|

4. Save your configuration.

.. _API Docs: http://taigaio.github.io/taiga-doc/dist/api.html
.. _mailing list: https://groups.google.com/forum/#!forum/taigaio

.. |Slack Integration Step 1| image:: /resources/contrib-plugins/slack-integration/slack-integration-1.png
.. |Slack Integration Step 2| image:: /resources/contrib-plugins/slack-integration/slack-integration-2.png
.. |Slack Integration Step 3| image:: /resources/contrib-plugins/slack-integration/slack-integration-3.png
.. |Slack Integration Step 4| image:: /resources/contrib-plugins/slack-integration/slack-integration-4.png
.. |Taiga Admin Slack Menu| image:: /resources/contrib-plugins/slack-integration/taiga-slack-menu.png
.. |Taiga Admin Slack Options| image:: /resources/contrib-plugins/slack-integration/taiga-slack-options.png
