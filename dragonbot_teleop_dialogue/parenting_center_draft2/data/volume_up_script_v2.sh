for i in *.wav; do /usr/bin/sox -v 2.0 "${i}" "${i%%.*}_v2.wav" ; done
