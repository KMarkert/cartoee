from __future__ import print_function

import warnings
import ee
import cartoee as cee
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ee.Initialize()

def mapTest(img,box,vis):
    ax = cee.getMap(img,region=box,visParams=vis,
                    cmap='gist_earth')
    plt.show()
    plt.close()


def layerTest(img,box,vis):
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax = cee.addLayer(img,ax=ax,region=box,visParams=vis,
                    cmap='gist_earth')
    plt.show()
    plt.close()


def colorbarTest(img,box,vis):
    ax = cee.getMap(img,region=box,visParams=vis,
                    cmap='gist_earth')
    cb = cee.addColorbar(ax,loc='right',cmap='gist_earth',visParams=vis)

    plt.show()
    plt.close()


def projectionTest(img,box,vis):
    projection = ccrs.Mollweide(central_longitude=-180)
    ax = plt.axes(projection=projection)

    ax = cee.addLayer(img,ax=ax,region=box,visParams=vis,
                    cmap='gist_earth')

    cb = cee.addColorbar(ax,loc='bottom',cmap='gist_earth',visParams=vis,
                         orientation='horizontal')

    plt.show()
    plt.close()


def main():
    visualization = {'min':-1000,'max':3000,'bands':'elevation'}
    bbox = [-180,-60,180,90]
    srtm = ee.Image("CGIAR/SRTM90_V4")

    print("Testing getMap functionality...")
    try:
        mapTest(srtm,bbox,visualization)
        print('getMap test successful')
        t1 = 'successful'
    except Exception as e:
        warnings.warn("getMap test failed...")
        t1 = 'failed'

    print("Testing addLayer functionality...")
    try:
        layerTest(srtm,bbox,visualization)
        print('addLayer test successful')
        t2 = 'successful'
    except Exception as e:
        warnings.warn("addLayer test failed...")
        t2 = 'failed'

    print("Testing colorbar functionality...")
    try:
        colorbarTest(srtm,bbox,visualization)
        print('colorbar test successful')
        t3 = 'successful'
    except Exception as e:
        warnings.warn("colorbar test failed...")
        t3 = 'failed'

    print("Testing projection functionality...")
    try:
        projectionTest(srtm,bbox,visualization)
        print('projection test successful')
        t4 = 'successful'
    except Exception as e:
        warnings.warn("colorbar test failed...")
        t4 = 'failed'

    print('Plotting testing done.\n '
          'getMap:      {0} \n '
          'addLayer:    {1} \n '
          'colorbar:    {2} \n '
          'projections: {3} \n '.format(t1,t2,t3,t4))
