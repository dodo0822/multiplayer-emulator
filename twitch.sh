#!/bin/bash

# streaming on Ubuntu via ffmpeg.
# see http://ubuntuguide.org/wiki/Screencasts for full documentation

# input resolution, currently fullscreen.
# you can set it manually in the format "WIDTHxHEIGHT" instead.
INRES="828x436"

# output resolution.
# keep the aspect ratio the same or your stream will not fill the display.
OUTRES="1280x720"

# input audio. You can use "/dev/dsp" for your primary audio input.
INAUD="pulse"

# target fps
FPS="30"

# video preset quality level.
# more FFMPEG presets avaiable in /usr/share/ffmpeg
QUAL="fast"

# stream key. You can set this manually, or reference it from a hidden file like what is done here.
STREAM_KEY=$(cat ~/.twitch_key)

# stream url. Note the formats for twitch.tv and justin.tv
# twitch:"rtmp://live.twitch.tv/app/$STREAM_KEY"
# justin:"rtmp://live.justin.tv/app/$STREAM_KEY"
STREAM_URL="rtmp://live-sin-backup.twitch.tv/app/$STREAM_KEY"

ffmpeg \
-f alsa -ac 2 -i "$INAUD" \
-f x11grab -s "$INRES" -r "$FPS" -i :0.0+3,60 \
-vcodec libx264 -s "$OUTRES" \
-pix_fmt yuv420p \
-acodec libmp3lame -threads 6 -qscale 5 -b 64KB \
-f flv -ar 44100 "$STREAM_URL"
