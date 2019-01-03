import ee
import numpy as np

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import cartopy.crs as ccrs
from cartopy.mpl.geoaxes import GeoAxesSubplot
import matplotlib.pyplot as plt

def plot(imgObj,proj=ccrs.PlateCarree(),dims=None,region=None,visParams=None,axes=None):
    """
    Create a cartopy plot with a geographic projection from an Earth Engine image object.

    Args:
        imgObj (ee.image.Image): Earth Engine image result to plot
        proj (cartopy.crs, optional): Cartopy projection that determines the projection of the resulting plot. By default uses an equirectangular projection, PlateCarree.
        dims (list or tuple or int, optional): dimensions to request earth engine result as [WIDTH,HEIGHT]. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. Default None and infers dimesions
        region (list or tuple, optional): geospatial region of the image to render in format [E,S,W,N]. By default, the whole image.
        visParams (dict, optional): visualization parameters as a dictionary. See https://developers.google.com/earth-engine/image_visualization for options.
        axes (cartopy.mpl.geoaxes.GeoAxesSubplot, optional): cartopy GeoAxesSubplot object. Default None and creates new one

    Returns:
        axes (cartopy.mpl.geoaxes.GeoAxesSubplot): cartopy GeoAxesSubplot object with Earth Engine results displayed

    Raises:
        ValueError: If `dims` is not of type list, tuple, or int
        ValueError: If `imgObj` is not of type ee.image.Image
        ValueError: If `axes` if not of type cartopy.mpl.geoaxes.GeoAxesSubplot'
    """

    if type(imgObj) != ee.image.Image:
        raise ValueError("provided imgObj is not of type ee.image.Image")

    if region:
        mapRegion = ee.Geometry.Rectangle(region).getInfo()['coordinates']
        viewExtent = (region[0],region[2],region[1],region[3])
    else:
        mapRegion = imgObj.geometry().bounds().getInfo()['coordinates']
        x,y = list(zip(*mapRegion[0]))
        viewExtent = [min(x),max(x),min(y),max(y)]

    if type(dims) == None and type(dims) not in [list,tuple,int]:
        raise ValueError('provided dims not of type list, tuple, or int')

    if type(axes) != GeoAxesSubplot:
        if axes == None:
            axes = plt.axes(projection=proj)
        else:
            raise ValueError('provided axes not of type cartopy.mpl.geoaxes.GeoAxesSubplot')

    args = {'format':'png'}
    if region:
        args['region'] = mapRegion
    if dims:
        args['dimensions'] = dims

    if visParams:
        keys = list(visParams.keys())
        for key in keys:
            args[key] = visParams[key]

    url = imgObj.getThumbUrl(args)

    img = urlopen(url)

    a = plt.imread(img)

    axes.imshow(a, extent=viewExtent,origin='upper',transform=ccrs.PlateCarree())

    return axes

if __name__ == "__main__":
    srtm = ee.Image("CGIAR/SRTM90_V4")
    test = plot(srtm,region=[-180,-90,180,90],visParams={min:0,max:3000})
    plt.show()
