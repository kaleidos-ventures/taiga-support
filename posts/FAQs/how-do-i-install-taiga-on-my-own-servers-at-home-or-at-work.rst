.. title: How do I install Taiga On My Own Servers At Home Or At Work?
.. slug: how-do-i-install-taiga-on-my-own-servers-at-home-or-at-work
.. date: 2015-10-15 18:08:41 UTC+02:00
.. tags: 
.. category:  FAQs
.. order: 60
.. link: 
.. description: 
.. type: text

*Taiga was designed to be as accessible as possible, and can be set up
on your own server. To make self-hosting very flexible, you have the
following options:*

Developer Mode
==============

It’s a manual process. You configure some services and it’s fast a
simple. This is ideal for those who want to play with Taiga in their own
local environment.

Check out `our documentation`_

Production mode
===============

This is also a manual installation. The process is a bit slower and more
complex, but will result in a solid, robust installation that can be
used comfortably on a development server for internal use. As a system
administrator you will need to have the knowledge to implement a variety
of tools required by the system

Check out `our documentation
<http://taigaio.github.io/taiga-doc/dist/#_setup_production_environment>`__

Using Taiga-scripts
===================

To simplify self-hosted installation we also created an automated
version of the developer installation mode using taiga-scripts. The
process should go smoothly, but If something does go wrong during this
automated process, you will need to fix errors by following the manual
deploy process.

Check out `our documentation
<http://taigaio.github.io/taiga-doc/dist/setup-alternatives.html#setup-taiga-scripts>`__

Using Taiga-vagrant
===================

`Vagrant`_ is a tool for building complete development environments.
With an easy-to-use workflow and focus on automation, Vagrant lowers
 development environment setup time, increases development/production
 parity, and makes the”works on my machine" excuse a relic of the past.

If you are a fan of Vagrant, you can use this method. Check out `our
documentation <http://taigaio.github.io/taiga-doc/dist/setup-alternatives.html#setup-taiga-vagrant>`__

.. _our documentation: http://taigaio.github.io/taiga-doc/dist/#_setup_development_environment
.. _Vagrant: https://www.vagrantup.com/about.html
