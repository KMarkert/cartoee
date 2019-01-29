Overview
===================================

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:


:code:`cartoee` is a simple Python package used for making publication quality
maps from `Earth Engine <https://earthengine.google.com/>`_ results using
`Cartopy <https://scitools.org.uk/cartopy/docs/latest/>`_ without having to
download results.

This packages aims to do only one thing well: getting processing results from
Earth Engine into a publication quality mapping interface. :code:`cartoee`
simply gets results from Earth Engine and plots it with the correct geographic
projections leaving :code:`ee` and :code:`cartopy` to do more of the processing
and visualization.

A typical Earth Engine workflow includes:

1. Processing your data on Earth Engine
2. Exporting your data from Earth Engine
3. Creating maps of your results

Here, we omit the 2nd step and merge steps 1 and 3 into one step. This allows
users to process their data using the Python Earth Engine API and quickly
create a map.

Installation
-------------

:code:`cartoee` is available to install via :code:`pip`. To install the package,
you can use pip  install for your Python environment:

.. code-block:: bash

  pip install cartoee

Or, you can install the package manually from source code using the following commands:

.. code-block:: bash

  git clone https://github.com/kmarkert/cartoee.git
  cd cartoee
  python setup.py install

Dependencies
~~~~~~~~~~~~~

:code:`cartoee` is built using pure Python code however relies on a few dependencies
(`earthengine-api <https://developers.google.com/earth-engine/>`_ and cartopy_)
that are available. These additional Python packages have their own dependencies
and users are referred to the dependencies documentation for full installation
instructions:

* `Matplotlib installation <https://matplotlib.org/users/installing.html>`_
* `Earth Engine API installation <https://developers.google.com/earth-engine/python_install_manual>`_
* `Cartopy installation <https://scitools.org.uk/cartopy/docs/latest/installing.html#installing>`_

Using the :code:`pip install` command will install all of the necessary dependencies
needed for using cartoee.

.. note::

    - Before installing cartoee, the cartopy requires the `GEOS
      <https://geos.osgeo.org/doxygen/>`_ and `Proj4
      <https://proj4.org/>`_ libraries installed on your system before
      being able to properly install.

Additional steps need to be taken to authenticate your local machine to use
the Earth Engine API. You can do this using the following command and follow
the instructions:

.. code-block:: bash

    earthengine authenticate


Another easy way to get dependencies installed correctly is to use conda for
matplotlib and cartopy prior to installing cartoee.
