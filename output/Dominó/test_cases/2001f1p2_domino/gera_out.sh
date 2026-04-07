#!/bin/sh

for i in `seq 1 20`; do
	for j in `seq 1 2`; do
		echo Gerando $i/out$j
		./sol < $i/in$j > $i/out$j
	done
done

