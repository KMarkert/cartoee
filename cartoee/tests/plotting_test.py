import ee
import cartoee as cee
import matplotlib.pyplot as plt

ee.Initialize()

visualization = {'min':-1000,'max':3000}
bbox = [-180,-60,180,90]
srtm = ee.Image("CGIAR/SRTM90_V4")

ax = cee.getMap(srtm,region=bbox,visParams=visualization,
                cmap='gist_earth',dims=2000)

plt.show()
