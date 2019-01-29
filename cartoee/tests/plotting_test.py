from __future__ import print_function

import warnings
import ee
import cartoee as cee
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ee.Initialize()

def mapTest(img,box,vis):
    plt.figure()
    ax = cee.getMap(img,region=box,visParams=vis,
                    cmap='gist_earth')
    plt.show()


def layerTest(img,box,vis):
    plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax = cee.addLayer(img,ax=ax,region=box,visParams=vis,
                    cmap='gist_earth')
    plt.show()


def colorbarTest(img,box,vis):
    plt.figure()
    ax = cee.getMap(img,region=box,visParams=vis,
                    cmap='gist_earth')
    cb = cee.addColorbar(ax,loc='right',cmap='gist_earth',visParams=vis)

    plt.show()


def projectionTest(img,box,vis):
    plt.figure()
    projection = ccrs.Mollweide(central_longitude=-180)
    ax = plt.axes(projection=projection)

    ax = cee.addLayer(img,ax=ax,region=box,visParams=vis,
                    cmap='gist_earth')

    cb = cee.addColorbar(ax,loc='bottom',cmap='gist_earth',visParams=vis)

    plt.show()


def main():
    visualization = {'min':-1000,'max':3000,'bands':'elevation'}
    bbox = [-180,-60,180,90]
    srtm = ee.Image("CGIAR/SRTM90_V4")

    print("Testing basin plotting functionality...")
    try:
        mapTest(srtm,bbox,visualization)
        print('Plotting successful')
    except Exception as e:
        warnings.warn("Plotting test failed...")
