.. cartoee documentation master file, created by
   sphinx-quickstart on Thu Jan  3 10:01:26 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

cartoee
===================================

:code:`cartoee` is a simple Python package used for making publication quality maps from `Earth Engine <https://earthengine.google.com/>`_ results using `Cartopy <https://scitools.org.uk/cartopy/docs/latest/>`_ without having to download results.

This packages aims to do only one thing well: getting processing results from Earth Engine into a publication quality mapping interface. :code:`cartoee` simply gets results from Earth Engine and plots it with the correct geographic projections leaving :code:`ee` and :code:`cartopy` to do more of the processing and visualization.


.. toctree::
   :maxdepth: 2
   :caption: Introduction:

   introduction.rst


.. toctree::
   :maxdepth: 2
   :caption: Examples:

   examples/cartoee_simple.ipynb
   examples/cartoee_projections.ipynb
   examples/cartoee_multimaps.ipynb


.. toctree::
  :maxdepth: 2
  :caption: API Reference:

  ToDo
