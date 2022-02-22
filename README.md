# Why This Project

To set the scene - a few friends had a bar out in Los Angeles - this is about 10 years ago, pre-covid. We are there, sampling a variety of beers and catching up on old times. Inexplicably, we are soon deep into a few hundred dollars of scratchers lottery tickets, which somehow fit the evening perfectly. And in the background, a movie played. At the movie's conclusion, the discussion turned to, what else can we play? And another movie was selected, but you soon realize that starting another movie from the beginning is not quite what the environment needed. And in that moment, an idea is hatched - why isn't there a simple way to randomly play movies, starting randomly, for a random duration, on a loop? 

# The Implementation

I had been helping my dad with some side projects involving microcontrollers - Arduinos and Raspberry PIs - and turned to the task at hand - can a microcontroller be used to solve the problem. And it turns out that the Raspberry PI 3 was perfectly suited to the task - HDMI outputs, video playback capabile, and a linux environment. Turns out that linux shell scripting is perfectly suited to the task. 

And so was born gregflix: a random video jukebox, playing only your favorite movies, in a random manner, perfect for a constantly churning environment, inspired by a brief lull in an otherwise memorable evening.

# Raspberry Pi 3 - Video Jukebox

This project is designed to take a Raspberry Pi 3 or later and use it as a video jukebox. Using bash scripting, onboard Raspberry PI video player, and a collection of MP4 movie files, the script will randomly play movies for a random duration. The inspiration for this project was a friend's bar, which would play movies while patrons were drinking. The downside of this approach is that if you didn't like the movie, it would be on for a few hours, so this approach adds some novelty to the mix. There are a few touches, like not playing the opening or closing credits using offsets, but otherwise this is a simple command line script that leverages the awesome capabilities of the Pi with an external hard drive. Enjoy!

https://stackoverflow.com/questions/4279611/how-to-embed-a-video-into-github-readme-md/4279746#4279746
