import ee
import cartoee as cee
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ee.Initialize()

def calc_ndvi(img):
    ndvi = img.normalizedDifference(['Nadir_Reflectance_Band2','Nadir_Reflectance_Band1'])
    return img.addBands(ndvi.rename('ndvi'))

table = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')

modis = ee.ImageCollection('MODIS/006/MCD43A4').filter(ee.Filter.date('2018-01-01', '2018-07-01')).map(calc_ndvi)

ax = cee.getMap(modis.median().updateMask(ndvi.lt(0)),visParams({'min':0.0,'max': 4000.0,'gamma':1.4,
        'bands':'Nadir_Reflectance_Band1,Nadir_Reflectance_Band4,Nadir_Reflectance_Band3'},
        region=[-180,-90,180,90],dims=1000,proj=ccrs.Orthographic(-5,33))

ocean = ee.ImageCollection('NASA/OCEANDATA/MODIS-Terra/L3SMI').filter(ee.Filter.date('2018-01-01', '2019-01-01'))

ax = cee.addLayer(ocean.median(),ax=ax,visParams={'bands':'chlor_a','min':0,'max':3,
        'palette':'27253d,0d627a,326765,7da87b,f5f5c6'},region=[-180,-90,180,90],
        dims=1000)

ax.coastlines()
ax.gridlines(linestyle=':')

plt.tight_layout()
plt.show()
