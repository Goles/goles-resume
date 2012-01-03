#!/usr/bin/python

import subprocess

def shell_exec(command):
	subprocess.call(command, shell=True)
	
def header_print(text):
	print("+\t" + text + "\t")
	
shell_exec("xelatex cv.tex; bibtex cv; xelatex cv.tex; xelatex cv.tex")