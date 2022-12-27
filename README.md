# software defined radio & gps

This is a project which never quite left the laboratory, but the idea here is to combine a software-defined radio (SDR), and a GPS device, both running on a raspberry pi, to take radio frequency (RF) measurements and log the physical location and altitude of the measurements taken. In theory, the Raspberry Pi and sensors could be mounted on a car, or a drone, to take multiple measurements and log all of the associated data.

I did not turn this into a working final product, but was able to get both the SDR and the GPS modules working to the point that I could take RF measurements and log GPS coordinates to demonstrate to myself that this could be done. This was part of a contemplated project for my dad's company, Power Technology Solutions (PTS).

# gregflix

gregflix is a self-contained, randomized personal video player running on a Raspberry Pi 3 or later. This project is a great example of the power of linux shell scripting as well as the Raspberry Pi itself. 

Required files:
* video.sh
* vncboot.sh - this is for remote access to the RPI using a VNC viewer
* Desktop Entry - this is how the video.sh is loaded. The bash script requires the location of the media drive, as well as the randomization

An example is below. This will play 3 minute clips and wait 30 seconds between clips. The desktop of the Raspberry Pi can be set to show a logo, which serves as advertising or other messaging when the video is not playing. Either time can be adjusted longer or shorter as needed.
```
/home/pi/video.sh /media/pi/Passport 180 30
```

Note that this project supposes that you have a personal collection of movies in MP4 or MKV format (something that can be played by ffmpeg on a Raspberry Pi). I encoded a bunch of my blu-ray DVDs to MP4s using Handbrake a number of years ago, which made this process a lot easier for me. The movies are copied to a Western Digital passport USB drive. The Raspberry Pi can't power this directly from its own USB ports, so a special adapter cable is required to power the drive.

## Background 

To set the scene - a few friends had a bar out in Los Angeles. We are sampling a variety of beers and catching up on old times. Inexplicably, we are soon deep into scratchers lottery tickets. And in the background, a movie played. At the movie's conclusion, the discussion turned to, what else can we play? And another movie was selected, but you soon realize that starting another movie from the beginning is not quite what the environment needed. And in that moment, an idea is hatched - what if we had a simple way to randomly play movies, at random star times, for random durations, on a loop? 

## The Implementation

A Raspberry Pi is perfectly suited to the task - low cost, self-contained, video playback capible, HDMI outputs, and runs on Linux. And, with an existing collection of movies in MP4 format, this project can be implemented with linux shell scripting. And so was born the gregflix  video jukebox, playing only your favorite movies, in a random manner, for a random duration, perfect for a constantly churning environment like a bar, inspired by a brief lull in an otherwise memorable evening.

The upside of this approach is that if you didn't like the movie, it would only be on for a short period of time, and the downside is that if you do like the movie, the time you get to watch it will be unpredicable and probably too short. 

There are a few extra touches, like not playing the opening or closing credits using offsets, but otherwise this is a simple command line script that leverages the awesome capabilities of the Pi with an external hard drive. 

Enjoy!

Raspberry Pi - this can be placed inside various enclosures available so it looks more aesthetically pleasing, or placed somewhere not visible. For the demo, I wanted to show the components involved.

![Raspberry Pi3](https://github.com/greg643/rpi/blob/master/rpi.jpg?raw=true)

