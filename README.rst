Masdap
========================

Start your server
-----------------

You need Docker 1.12 or higher.

1. Run `docker-compose` to start it up

   .. code:: bash

     docker-compose build --no-cache
     docker-compose up -d
     
   **NOTE for Windows users**: In case you're using the native Docker for Windows (on Hyper-V) you will probably be affected by an error related to mounting the /var/run/docker.sock volume. It's due to a `problem with the current version of Docker Compose <https://github.com/docker/for-win/issues/1829>`_ for Windows.
   In this case you need to set the **COMPOSE_CONVERT_WINDOWS_PATHS** environmental variable:
   
   .. code-block:: none
   
      set COMPOSE_CONVERT_WINDOWS_PATHS=1 
   
   before running docker-compose up

2. Access the site on http://localhost/


If you want to run the instance on a public site
------------------------------------------------

Preparation of the image (First time only)
++++++++++++++++++++++++++++++++++++++++++

.. note:: In this example we are going to publish to the public IP http://123.456.789.111

.. code:: bash

  vim docker-compose.override.yml
    --> replace localhost with 123.456.789.111 everywhere

Startup the image
+++++++++++++++++

.. code:: bash

  docker-compose up --build -d


To Stop the Docker Images
-------------------------

.. code:: bash

  docker-compose stop


To Fully Wipe-out the Docker Images
-----------------------------------

.. warning:: This will wipe out all the repositories created until now.

.. note:: The images must be stopped first

.. code:: bash

  docker system prune -a
