from __future__ import print_function

import subprocess
import setuptools
from setuptools import setup
from setuptools.command.install import install

class eeAuthCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        print("Authorizing the Earth Engine API on your environment...")

        import ee
        from ee.ee_exception import EEException

        # try to initialize Earth Engine session
        try:
          ee.Initialize()

        # if it doesn't work, then authorize an account for Earth Engine to connect to...
        except EEException:
          !earthengine authenticate --quiet

          authCode = input("Authorization code:")

          subprocess("earthengine authenticate --authorization-code=$authCode")

          # ...then initialize session
          ee.Initialize()
          print("Authorization successful!")

        install.run(self)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cartoee',
      version='0.0.4',
      description='Publication quality maps using Earth Engine and Cartopy!',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/kmarkert/cartoee',
      packages=setuptools.find_packages(),
      author='Kel Markert',
      author_email='kel.markert@gmail.com',
      license='GNU GPL v3',
      zip_safe=False,
      include_package_data=True,
      install_requires=[
          'matplotlib',
          'Cython',
          'geos',
          'pyproj',
          'cartopy==0.16.0',
          'oauth2client',
          'google-api-python-client',
          'earthengine-api',
      ],
      cmdclass={
        'install': eeAuthCommand,
        },
)
