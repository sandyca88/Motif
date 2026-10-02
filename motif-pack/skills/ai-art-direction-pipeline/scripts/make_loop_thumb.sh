#!/usr/bin/env bash
# Composite a UI overlay on an AI video and export a light animated thumbnail + poster.
# usage: make_loop_thumb.sh input.mp4 overlay.png out-basename   (overlay must be 1152x720 for a 1280x720 source)
set -euo pipefail
IN="$1"; OV="$2"; OUT="$3"
ffmpeg -v error -y -i "$IN" -i "$OV" -filter_complex "[0:v]crop=ih*1.6:ih:(iw-ih*1.6)/2:0[v];[v][1:v]overlay=0:0,scale=960:600:flags=lanczos,format=yuv420p" \
  -an -c:v libx264 -preset slow -crf 27 -movflags +faststart "$OUT.mp4"
ffmpeg -v error -y -ss 3 -i "$OUT.mp4" -frames:v 1 -q:v 3 "$OUT-poster.jpg"
echo "saved $OUT.mp4 and $OUT-poster.jpg"
