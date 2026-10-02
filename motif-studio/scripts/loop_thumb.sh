#!/usr/bin/env bash
# Seamless animated thumbnail from an AI video.
# usage: loop_thumb.sh in.mp4 out.mp4 [start=0] [end=7] [fade=1.5]
# Crops 16:9 -> 16:10, scales to 960x600 @24fps, no audio, and crossfades the tail into the head
# so the clip loops without a jump. Output length = end - start - fade seconds.
set -euo pipefail
IN="$1"; OUT="$2"; S="${3:-0}"; E="${4:-7}"; F="${5:-1.5}"
calc(){ python3 -c "print($1)"; }
L=$(calc "$E-$S-$F"); A=$(calc "$S+$F"); OFF=$(calc "$L-$F")
ffmpeg -v error -y -i "$IN" -filter_complex \
 "[0:v]crop=ih*1.6:ih:(iw-ih*1.6)/2:0,scale=960:600:flags=lanczos,fps=24,split[a][b];\
[a]trim=$A:$E,setpts=PTS-STARTPTS[m];[b]trim=$S:$A,setpts=PTS-STARTPTS[h];\
[m][h]xfade=transition=fade:duration=$F:offset=$OFF,format=yuv420p" \
 -an -c:v libx264 -preset slow -crf 26 -movflags +faststart "$OUT"
echo "saved $OUT ($(du -h "$OUT" | cut -f1), $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")s)"
