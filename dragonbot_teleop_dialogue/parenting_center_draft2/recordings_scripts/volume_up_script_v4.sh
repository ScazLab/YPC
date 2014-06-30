for i in *v2.wav; do /usr/bin/sox -v 2.0 "${i}" "${i%%.*}_v4.wav" ; done
