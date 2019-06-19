***************
Simple Payroll
***************

Setup
=====

No local setup should be needed apart from:

- `docker <https://docs.docker.com/engine/installation/>`__
- `docker-compose <https://docs.docker.com/compose/>`__

Build the app
-------------

Run in project directory:

.. code:: bash

    docker-compose build

Run the server
--------------

Run in project directory:

.. code:: bash

    docker-compose up


This will build the container based on the Dockerfile and docker-compose file
and start the local server at ``http://localhost:8080``
