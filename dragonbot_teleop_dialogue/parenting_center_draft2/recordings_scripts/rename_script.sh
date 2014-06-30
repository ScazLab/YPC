for filename in *.wav; do
	mv $filename ${filename//_v2/}
done
