#!/bin/bash


YEARS=$(cat years.txt)
for YEAR in $YEARS
do
	echo "$YEAR"
	grep "^$YEAR" raw.dat | head > raw"$YEAR".dat
done	
