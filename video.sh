#!/bin/bash
#Command Line Arguments
#1 = Directory
#2 = Duration to Play
#3 = Duration to sleep between videos

 # get movies
files=($1/*.{mp4,m4v,mkv})

sleepseconds=$3

if [ -t 0 ]; then stty -echo -icanon -icrnl time 0 min 0; fi

count=0
keypress=''
while [ "x$keypress" = "x" ]; do
  let count+=1
  echo -ne $count'\r'
  keypress="`cat -v`"


# pick one randomly
n=${#files[@]}
movieplay="${files[RANDOM % n]}"
echo "$movieplay"

#start_mins=$(((RANDOM % 40)  + 5))
#start_time="00:$start_mins:00"

#echo "$start_mins"
#echo "$start_time"

to_seconds () {
    response=$(awk -F':' '{print $1 * 60 * 60 + $2 * 60 + $3}')
echo $response
}

#get duration of movie
duration=$(ffmpeg -i "$movieplay" 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//)
echo "$duration"
#to_seconds $duration

testString="abcdefg:12345:67890:abcde:12345:abcde"
timeString="$duration"
IFS=':'
array=( $timeString )
time1=${array[0]}
time2=${array[1]}
echo "$time1"
echo "$time2"

start_hour=0
if [ $time1 -gt 0 ]
then
start_hour=$(((RANDOM % $time1)  + 0))
fi

start_mins=3
time2n=$(echo $time2 | sed 's/^0*//')
if [ $time2n -gt 3 ]
then
start_mins=$(((RANDOM % $time2n)  + 3))
fi

start_time="$start_hour:$start_mins:00"

echo "$start_mins"
echo "$start_hour"
echo "$start_time"

#play movie
expect -c "spawn omxplayer -l $start_time -o hdmi $movieplay --no-osd; sleep $2; send q; interact"

sleep $sleepseconds

done

if [ -t 0 ]; then stty sane; fi

echo "You pressed '$keypress' after $count loop iterations"
echo "Thanks for using this script."
exit 0
