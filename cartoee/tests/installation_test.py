from __future__ import print_function
import warnings
import subprocess

def main():
    try:
        import matplotlib.pyplot as plt
        print('Successfully imported matplotlib\n')

    except ImportError:
        warnings.warn("Could not import matplotlib...\n")

    try:
        import ee
        from ee.ee_exception import EEException
        print('Successfully imported ee\n')

        # try to initialize Earth Engine session
        try:
            ee.Initialize()
            print('Successfully initialized and ee session\n')

        # if it doesn't work, then authorize an account for Earth Engine to connect to...
        except EEException:
            print('Trying to authorize your ee account...\n')
            subprocess.call('earthengine authenticate --quiet',shell=True)

            authCode = input("Authorization code:")

            subprocess.call('earthengine authenticate --authorization-code={}'.format(authCode),
                            shell=True)

            try:
                # ...then initialize session
                ee.Initialize()
                print('Successfully initialized and ee session\n')

            # if it doesn't work, then throw warning...
            except EEException:
                warnings.warn("Could not import initialize ee session...\n")

    except ImportError:
        warnings.warn("Could not import ee...\n")

    try:
        import cartopy
        import cartopy.crs as ccrs
        print('Successfully imported cartopy\n')

    except:
        warnings.warn("Could not import cartopy...\n")

    try:
        import cartoee as cee
        print('Successfully imported cartoee\n')

    except:
        warnings.warn("Could not import cartoee...\n")

    print('Installation testing done.')
