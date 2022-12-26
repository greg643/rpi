# gregflix

## Background 

To set the scene - a few friends had a bar out in Los Angeles. We are sampling a variety of beers and catching up on old times. Inexplicably, we are soon deep into scratchers lottery tickets. And in the background, a movie played. At the movie's conclusion, the discussion turned to, what else can we play? And another movie was selected, but you soon realize that starting another movie from the beginning is not quite what the environment needed. And in that moment, an idea is hatched - what if we had a simple way to randomly play movies, at random star times, for random durations, on a loop? 

## The Implementation

A Raspberry Pi is perfectly suited to the task - low cost, self-contained, video playback capible, HDMI outputs, and runs on Linux. And, with an existing collection of movies in MP4 format, this project can be implemented with linux shell scripting. And so was born the gregflix  video jukebox, playing only your favorite movies, in a random manner, for a random duration, perfect for a constantly churning environment like a bar, inspired by a brief lull in an otherwise memorable evening.

The upside of this approach is that if you didn't like the movie, it would only be on for a short period of time, and the downside is that if you do like the movie, the time you get to watch it will be unpredicable and probably too short. 

There are a few extra touches, like not playing the opening or closing credits using offsets, but otherwise this is a simple command line script that leverages the awesome capabilities of the Pi with an external hard drive. 

Enjoy!

https://stackoverflow.com/questions/4279611/how-to-embed-a-video-into-github-readme-md/4279746#4279746
