import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cartoee',
      version='0.0.2',
      description='Publication quality maps using Earth Engine and Cartopy!',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/kmarkert/cartoee',
      packages=setuptools.find_packages(),
      author='Kel Markert',
      author_email='kel.markert@gmail.com',
      license='GNU GPL',
      zip_safe=False,
      include_package_data=True,
)
