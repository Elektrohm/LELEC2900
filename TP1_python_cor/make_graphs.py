import matplotlib.pyplot as plt

import numpy as np 

import os
root = os.getcwd()
from pathlib import Path


plt.rc('font',  size=10)
plt.rc('xtick', labelsize=10) 
plt.rc('ytick', labelsize=10) 
plt.rc('axes',  titlesize=10)


"""
plotSignal plots a continuous time signal (y depeding of x) with optional arguments to comment the plot
INPUTS : 
    - x (time axis) and y (signal amplitude).
    - (Opt.) x_label/y_label: label for x and y axis respectively.
    - (Opt.) tile: plot's title
"""
def plotSignal(x, y, x_label='', y_label='', title=''): 
    fig,ax = plt.subplots(figsize=(9,3))  
    plt.plot(x,y)   
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

"""
plotSignalAndDft makes two subplots (the fist for the time signal and the second for the DFT): 
    1. a continuous time signal (y1 depeding of x1) 
    2. a discrete time signal (y2 depeding of x2) 
with optional arguments to comment the plots
INPUTS : 
    - x1 (time axis) and y2 (signal amplitude).
    - x1 (frequency axis) and y2 (spectrum amplitude).
    - (Opt.) x_label/y_label: label for x and y axis respectively.
    - (Opt.) tile: plot's title
"""
    
def plotSignalAndDft(x1, y1, x2, y2, xlim, x_label=['',''], y_label=['',''], title=''): 
    fig = plt.figure(figsize=(9,3))  
    # Subfigure 1 - Continuous time plot
    ax1 = fig.add_subplot(121) 
    ax1.plot(x1,y1)   
    ax1.set_xlabel(x_label[0])
    ax1.set_ylabel(y_label[0])
    # Subfigure 2 - Discrete time plot
    ax2 = fig.add_subplot(122) 
    ax2.stem(x2,y2, basefmt=" ") 
    ax2.set_xlim(xlim)
    ax2.set_xlabel(x_label[1])
    ax2.set_ylabel(y_label[1])
    plt.title(title)
    plt.show()
