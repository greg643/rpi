import gps
from rtlsdr import RtlSdr

#must initiate gpsd from terminal before running
#https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/setting-everything-up
#sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

#GPS setup
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

#SDR setup
sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

##Available Attributes
#report.lat - latitude
#report.lon - longitude
#report.alt - altitude
#report.elv - elevation
#report.speed - speed

print(sdr.read_samples(128))

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
                #print(report)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")

