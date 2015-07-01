#Makefile for the Rameau Python version

all: clean long run

long: 
	python LongCorrection.py

run: 
	python Rameau.py

clean: 
	rm -rf ./plots/*
	rm -rf ./corrspectra/*
	rm RatioAndWater.pdf
	rm output.txt


