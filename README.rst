A python module for interacting with various parts of Steam_.

A fork of `ValvePython/steam <https://github.com/ValvePython/steam>`_, which has apparently been abandoned.

Currently supports Python ``3.10``, ``3.11``, and ``3.12``. We intend to support Python ``3.9-3.13`` and PyPy ``3.11``.

Documentation (**WARNING** - out of date): http://steam.readthedocs.io/en/latest/

Features
--------

* `SteamClient <http://steam.readthedocs.io/en/latest/api/steam.client.html>`_ - communication with the steam network based on ``gevent``.
* `CDNClient <http://steam.readthedocs.io/en/latest/api/steam.client.cdn.html>`_ - access to Steam content depots
* `WebAuth <http://steam.readthedocs.io/en/latest/api/steam.webauth.html>`_ - authentication for access to ``store.steampowered.com`` and ``steamcommunity.com``
* `WebAPI <http://steam.readthedocs.io/en/latest/api/steam.webapi.html>`_ - simple API for Steam's Web API with automatic population of interfaces
* `SteamAuthenticator <http://steam.readthedocs.io/en/latest/api/steam.guard.html>`_ - enable/disable/manage two factor authentication for Steam accounts
* `SteamID <http://steam.readthedocs.io/en/latest/api/steam.steamid.html>`_  - convert between the various ID representations with ease
* `Master Server Query Protocol <https://steam.readthedocs.io/en/latest/api/steam.game_servers.html>`_ - query masters servers directly or via ``SteamClient``

Checkout the `User guide <http://steam.readthedocs.io/en/latest/user_guide.html>`_ for examples,
or the `API Reference <http://steam.readthedocs.io/en/latest/api/steam.html>`_ for details.

For questions, issues or general curiosity visit the repo at `https://github.com/solsticegamestudios/steam <https://github.com/solsticegamestudios/steam>`_.

Like using the command line? Try `steamctl <https://github.com/ValvePython/steamctl>`_ tool

Install
-------

For system specific details, see `Installation Details <http://steam.readthedocs.io/en/latest/install.html>`_.

**WARNING:** Only ValvePython's (out of date) version is on PyPI.

Installing directly from ``github`` repository:

.. code:: bash

    # cutting edge from master
    pip install "git+https://github.com/solsticegamestudios/steam#egg=steam"

    # specific version tag (e.g. v1.0.0)
    pip install "git+https://github.com/solsticegamestudios/steam@v1.0.0#egg=steam[client]"
    # without SteamClient extras
    pip install "git+https://github.com/solsticegamestudios/steam@v1.0.0#egg=steam"

Vagrant
-------

The repo includes a `Vagrantfile` to setup environment for experimentation and development.
We assume you've already have ``vagrant`` and ``virtualbox`` set up.
The VM is ``Ubuntu 16.04`` with all necessary packages installed, and virtualenv for ``python2`` and ``python3``.


.. code:: bash

    vagrant up    # spin the VM and let it setup
    vagrant ssh
    # for python2
    $ source venv2/bin/activate
    # for python3
    $ source venv3/bin/activate



Local Testing
-------------

To run the test suite with the current ``python``, use

.. code:: bash

    make test

To run for specific version, setup a virtual environment

.. code:: bash

    virtualenv -p python3 py3
    source py3/bin/active
    pip install -r requirements.txt
    make test


.. _Steam: https://store.steampowered.com/
