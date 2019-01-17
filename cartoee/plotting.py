from __future__ import print_function, division
import ee
import warnings
import numpy as np
import matplotlib as mpl
from matplotlib import cm, colors
import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import cartopy.crs as ccrs
from cartopy.mpl.geoaxes import GeoAxes,GeoAxesSubplot


def getMap(imgObj,proj=ccrs.PlateCarree(),**kwargs):
    """
    Wrapper function to create a new cartopy plot with project and adds Earth
    Engine image results

    Args:
        imgObj (ee.image.Image): Earth Engine image result to plot
        proj (cartopy.crs, optional): Cartopy projection that determines the projection of the resulting plot. By default uses an equirectangular projection, PlateCarree
        **kwargs: remaining keyword arguments are passed to addLayer()

    Returns:
        ax (cartopy.mpl.geoaxes.GeoAxesSubplot): cartopy GeoAxesSubplot object with Earth Engine results displayed
    """

    ax = plt.axes(projection=proj)
    ax = addLayer(imgObj,ax=ax,**kwargs)

    return ax


def addLayer(imgObj,ax,dims=None,region=None,cmap=None,visParams=None):
    """
    Add an Earth Engine image to a cartopy plot.

    Args:
        imgObj (ee.image.Image): Earth Engine image result to plot.
        ax (cartopy.mpl.geoaxes.GeoAxesSubplot | cartopy.mpl.geoaxes.GeoAxes): required cartopy GeoAxesSubplot object to add image overlay to
        dims (list | tuple | int, optional): dimensions to request earth engine result as [WIDTH,HEIGHT]. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. Default None and infers dimesions
        region (list | tuple, optional): geospatial region of the image to render in format [E,S,W,N]. By default, the whole image
        cmap (str, optional): string specifying matplotlib colormap to colorize image. If cmap is specified visParams cannot contain 'palette' key
        visParams (dict, optional): visualization parameters as a dictionary. See https://developers.google.com/earth-engine/image_visualization for options

    Returns:
        ax (cartopy.mpl.geoaxes.GeoAxesSubplot): cartopy GeoAxesSubplot object with Earth Engine results displayed

    Raises:
        ValueError: If `dims` is not of type list, tuple, or int
        ValueError: If `imgObj` is not of type ee.image.Image
        ValueError: If `ax` if not of type cartopy.mpl.geoaxes.GeoAxesSubplot '
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

    if type(ax) not in [GeoAxes,GeoAxesSubplot]:
        raise ValueError('provided axes not of type cartopy.mpl.geoaxes.GeoAxes '
                         'or cartopy.mpl.geoaxes.GeoAxesSubplot')

    args = {'format':'png'}
    if region:
        args['region'] = mapRegion
    if dims:
        args['dimensions'] = dims

    if visParams:
        keys = list(visParams.keys())
        if cmap and ('palette' in keys):
            raise KeyError('cannot provide "palette" in visParams if cmap is specified')
        elif cmap:
            args['palette'] = ','.join(buildPalette(cmap))
        else:
            pass

        for key in keys:
            args[key] = visParams[key]

    url = imgObj.getThumbUrl(args)
    img = urlopen(url)
    a = plt.imread(img)

    ax.imshow(a, extent=viewExtent,origin='upper',transform=ccrs.PlateCarree())

    return ax

def buildPalette(cmap,n=256):
    """
    Creates hex color code palette from a matplotlib colormap

    Args:
        cmap (str): string specifying matplotlib colormap to colorize image. If cmap is specified visParams cannot contain 'palette' key
        n (int, optional): Number of hex color codes to create from colormap. Default is 256

    Returns:
        palette (list): list of hex color codes from matplotlib colormap for n intervals
    """

    colormap = cm.get_cmap(cmap, n)
    vals = np.linspace(0,1,n)
    palette = list(map(lambda x: colors.rgb2hex(colormap(x)[:3]),vals))

    return palette


def addColorbar(ax,loc=None,visParams=None,discrete=False,**kwargs):
    """
    Add a colorbar tp the map based on visualization parameters provided

    Args:
        ax (cartopy.mpl.geoaxes.GeoAxesSubplot | cartopy.mpl.geoaxes.GeoAxes): required cartopy GeoAxesSubplot object to add image overlay to
        loc (str, optional): string specifying the position
        visParams (dict, optional): visualization parameters as a dictionary. See https://developers.google.com/earth-engine/image_visualization for options
        **kwargs: remaining keyword arguments are passed to colorbar()

    Returns:
        cb (matplotlib.colorbar.ColorbarBase): matplotlib colorbar object

    Raises:
        Warning: If 'discrete' is true when "palette" key is not in visParams
        ValueError: If `ax` is not of type cartopy.mpl.geoaxes.GeoAxesSubplot
        ValueError: If 'cmap' or "palette" key in visParams is not provided
        ValueError: If "min" in visParams is not of type scalar
        ValueError: If "max" in visParams is not of type scalar
        ValueError: If 'loc' or 'cax' keywords are not provided
        ValueError: If 'loc' is not of type str or does not equal available options
    """

    if type(ax) not in [GeoAxes,GeoAxesSubplot]:
        raise ValueError('provided axes not of type cartopy.mpl.geoaxes.GeoAxes '
                         'or cartopy.mpl.geoaxes.GeoAxesSubplot')

    if loc:
        if (type(loc) == str) and (loc in ['left','right','bottom','top']):
            posOpts = {'left':   [0.01, 0.25, 0.02, 0.5],
                       'right':  [0.88, 0.25, 0.02, 0.5],
                       'bottom': [0.25, 0.15, 0.5, 0.02],
                       'top':    [0.25, 0.88, 0.5, 0.02]}

            cax = ax.figure.add_axes(posOpts[loc])

            if loc == 'left':
                plt.subplots_adjust(left=0.18)
            elif loc == 'right':
                plt.subplots_adjust(right=0.85)
            else:
                pass

        else:
            raise ValueError('provided loc not of type str. options are "left", '
                             '"top", "right", or "bottom"')

    elif cax:
        if type(cax) not in [Axes]:
            raise ValueError('provided cax not of type matplotlib.axes._axes.Axes')

    else:
        raise ValueError('loc or cax keywords must be specified')

    visKeys = list(visParams.keys())
    if visParams:
        if 'min' in visParams:
            vmin = visParams['min']
            if type(vmin) not in (int,float):
                raise ValueError('provided min value not of type scalar')
        else:
            vmin = 0

        if 'max' in visParams:
            vmax = visParams['max']
            if type(vmax) not in (int,float):
                raise ValueError('provided max value not of type scalar')
        else:
            vmax = 1

        if 'opacity' in visParams:
            alpha = visParams['opacity']
            if type(alpha) not in (int,float):
                raise ValueError('provided opacity value of not type scalar')
        elif 'alpha' in kwargs:
            alpha = kwargs['alpha']
        else:
            alpha = 1

        if 'palette' in visKeys:
            hexcodes = visParams['palette'].split(',')
            hexcodes = [i if i[0]=='#' else '#'+i for i in hexcodes]

            if discrete:
                cmap = mpl.colors.ListedColormap(hexcodes)
                vals = np.linspace(vmin,vmax,cmap.N+1)
                norm = mpl.colors.BoundaryNorm(vals, cmap.N)

            else:
                print(hexcodes)
                cmap = mpl.colors.LinearSegmentedColormap.from_list('custom', hexcodes, N=256)
                norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

            kwargs['cmap'] = cmap

        elif 'cmap' in kwargs:
            if discrete:
                warnings.warn('discrete keyword used when "palette" key is '
                              'supplied with visParams, creating a continuous '
                              'colorbar...')

            norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

        else:
            raise ValueError('cmap keyword or "palette" key in visParams must be provided')

    cb = mpl.colorbar.ColorbarBase(cax,norm=norm,alpha=alpha,
                                    **kwargs)

    if 'bands' in visKeys:
        cb.set_label(visParams['bands'])

    return cb


if __name__ == "__main__":
    srtm = ee.Image("CGIAR/SRTM90_V4")
    test = plot(srtm,region=[-180,-90,180,90],visParams={min:0,max:3000})
    plt.show()
