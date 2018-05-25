#!/usr/bin/python3
import timeit
import time
import os
import matplotlib.pyplot as plt 
from tqdm import trange
from injectSeed import *
from subprocess import call

def getRuntime(bytecode):
	""" executes program and returns running time """
	start = time.time()
	exec(bytecode)
	end = time.time()
	return end-start

def getRunTime_R(bytecode):
	start = time.time()
	exec(bytecode, globals())
	end = time.time()
	return end-start

def trialRun(bytecode, n, runtimeFunc):
	""" executes program using parameter n """
	bytecode = injectRandList(bytecode, n)
	runtime = runtimeFunc(bytecode)
	return runtime

def conductTrials(filename, n, runtimeFunc):
	trials = list()
	bytecode = open(filename).read()
	for i in trange(n, desc=filename.split('/')[-1]):
		trials.append(trialRun(bytecode, i, runtimeFunc))
	return trials

def plotRuntime(runtimes, n, name):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	axi = [i for i in range(n)]
	print()
	print("Plotting {}...".format(name))
	plt.plot(axi, runtimes, 'bo', markersize=0.5)
	plt.savefig("plots/Sorting/{}".format(name))
	plt.close()

def plotSortingAlg(n):
	bubblesorts = conductTrials("samples/Sorting/bubblesort.py", n, getRuntime)
	insertionsorts = conductTrials("samples/Sorting/insertionsort.py", n, getRuntime)
	mergesorts = conductTrials("samples/Sorting/mergesort.py", n, getRunTime_R)
	selectionsorts = conductTrials("samples/Sorting/selectionsort.py", n, getRuntime)
	quicksorts = conductTrials("samples/Sorting/quicksort.py", n, getRunTime_R)
	shellsorts = conductTrials("samples/Sorting/shellsort.py", n, getRuntime)
	heapsorts = conductTrials("samples/Sorting/heapsort.py", n, getRunTime_R)

	plotRuntime(bubblesorts, n, "bubblesorts.png")
	plotRuntime(insertionsorts, n, "insertionsorts.png")
	plotRuntime(mergesorts, n, "mergesorts.png")
	plotRuntime(selectionsorts, n, "selectionsorts.png")
	plotRuntime(quicksorts, n, "quicksorts.png")
	plotRuntime(shellsorts, n, "shellsorts.png")
	plotRuntime(heapsorts, n, "heapsorts.png")


def main():
	plotSortingAlg(10000)
main()
