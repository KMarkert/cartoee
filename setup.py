import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cartoee',
      version='0.0.5',
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
      entry_points={
        'console_scripts': [
            'cee_install_test = cartoee.tests.installation_test:main',
            'cee_plotting_test = cartoee.tests.plotting_test:main'
        ],
      },
)
