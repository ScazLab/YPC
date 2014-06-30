for i in *.aif; do /usr/bin/sox "${i}" "${i%%.*}_converted-100.wav" pitch -100 ; done
