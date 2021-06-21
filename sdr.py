# -*- coding: utf-8 -*-
#Created on Sun Jun 20 00:25:45 2021
#@author: greg

##GPSD
#import gps
from math import radians, degrees, sin, cos, asin, acos, sqrt
from geopy.distance import distance
from geopy.distance import great_circle
from geopy.point import Point

#SDR
from rtlsdr import RtlSdr

##PLOT SDR
# includes core parts of numpy, matplotlib
import matplotlib.pyplot as plt
import numpy as np
# include scipy's signal processing functions
import scipy.signal as signal

a = Point(41.49008,-71.312796, 0)
b = Point( 41.499498,-81.695391, 0)
print("geopy geodesic distance miles: " + str(distance(a, b).miles))
print("great circle distance miles: " + str(great_circle(a, b).miles))
#538.3904453677203

alat = -71.312796
alon = 41.49008

blat = -81.695391
blon = 41.499498

def great_circle(lat1, lon1, lat2, lon2, kmMiles):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    if kmMiles == "miles":
        radVal = 3958.756
    else:
        radVal = 6371
        
    return radVal * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )

print("great circle 2 distance miles: " + str(great_circle( alon, alat, blon, blat, "miles")))

#must initiate gpsd from terminal before running
#https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/setting-everything-up
#sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

#complex_nums_list = [2+3j, 3+4j, 4+5j]
#plt.psd(complex_nums_list, NFFT=1024, Fs=1000000)
#plt.title("PSD of 'signal' loaded from file")
#plt.show() 

#SDR setup
sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 220e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

##Available Attributes
#report.lat - latitude
#report.lon - longitude
#report.alt - altitude
#report.elv - elevation
#report.speed - speed

sdr_output = sdr.read_samples(128)

# print(sdr.read_samples(128))

plt.psd(sdr_output, NFFT=1024, Fs=1000000)
plt.title("PSD of 'signal' loaded from file")
plt.show() 

# https://pysdr.org/content/sampling.html#calculating-average-power
avg_pwr = np.mean(np.abs(sdr_output)**2)
print("sample rate: " + str(sdr.sample_rate))
print("center freq: " + str(sdr.center_freq))
print("freq correction: " + str(sdr.freq_correction))
print("avg power: " + str(avg_pwr))


sdr.close() ##unbind for end of program


############
###GPS Setup
############

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print(report)
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                gtime = report.time
                glat = str(report.lat)
                glon = str(report.lon)  
                galt = str(report.alt)
                #print(sdr.read_samples(512))
                print(report.time + "," + glat + "," + glon + "," + galt)
                print("distance report " + great_circle( alon, alat, report.lat, report.lon, "miles"))
                #print(report)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
