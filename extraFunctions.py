import os,time,sys,signal, subprocess

def cmove (y, x):
    print("\033[%d;%dH"%(y, x))

# def fmove (x):
#     print("\033[P%dC" %(x))
