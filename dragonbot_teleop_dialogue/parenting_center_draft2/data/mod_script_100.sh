for i in *.aif; do /usr/bin/sox "${i}" "${i%%.*}_c100.wav" pitch 100 ; done
