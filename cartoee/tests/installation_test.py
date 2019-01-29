from __future__ import print_function
import warnings
import subprocess

def main():
    try:
        import matplotlib.pyplot as plt
        print('Successfully imported matplotlib')

    except ImportError:
        warnings.warn("Could not import matplotlib...")

    try:
        import ee
        from ee.ee_exception import EEException
        print('Successfully imported ee')

        # try to initialize Earth Engine session
        try:
            ee.Initialize()
            print('Successfully initialized and ee session')

        # if it doesn't work, then authorize an account for Earth Engine to connect to...
        except EEException:
            subprocess.call('earthengine authenticate --quiet',shell=True)

            authCode = input("Authorization code:")

            subprocess.call('earthengine authenticate --authorization-code={}'.format(authCode),
                            shell=True)

            # ...then initialize session
            ee.Initialize()
            print('Successfully initialized and ee session')

        finally:
            warnings.warn("Could not import initialize ee session...")

    except ImportError:
        warnings.warn("Could not import ee...")

    try:
        import cartopy
        import cartopy.crs as ccrs
        print('Successfully imported cartopy')

    except:
        warnings.warn("Could not import cartopy...")

    try:
        import cartoee as cee
        print('Successfully imported cartoee')

    except:
        warnings.warn("Could not import cartoee...")
