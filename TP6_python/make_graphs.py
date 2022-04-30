import matplotlib.pyplot as plt

import numpy as np 

import os
root = os.getcwd()
from pathlib import Path

plt.rc('xtick', labelsize=16) 
plt.rc('ytick', labelsize=16) 
plt.rcParams.update({'font.size': 16}) 


"""--------------------------------------------------------------------------------------------------
Plot the wavelet decomposition of a singal based on the (previously) computed approximation and 
detail coefficients.
INPUTS: 
    - signal : original sigal vector (without time)
    - coeefs : DWT coefficients in the following order : [cA_n, cD_n, cD_n-1, …, cD_2, cD_1]
--------------------------------------------------------------------------------------------------"""
def print_decomposition(signal, coeffs):
    approx_coeffs, detail_coeffs = coeffs[0], coeffs[1:]
    fig = plt.figure(figsize=(20,10))
    ax_main = fig.add_subplot(len(detail_coeffs) + 1, 1, 1)
    ax_main.plot(signal, linewidth=1)
    ax_main.set_xlim(0, len(signal) - 1)
    ax_main.get_xaxis().set_visible(False)
    ax_main.get_yaxis().set_visible(False)

    ax = fig.add_subplot(len(detail_coeffs) + 1, 2, 3 )
    ax.plot(approx_coeffs, 'teal', linewidth=1)
    ax.set_xlim(0, len(approx_coeffs) - 1)
    ax.patch.set_alpha(0)
    #ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    plt.text(-(len(approx_coeffs) - 1)*0.15, np.mean(approx_coeffs), "A%d" % len(detail_coeffs))

    for i, y in enumerate(detail_coeffs[::-1]):
        ax = fig.add_subplot(len(detail_coeffs) + 1, 2, 4 + i * 2)
        ax.plot(y, 'crimson', linewidth=1)
        ax.set_xlim(0, len(y) - 1)
        #ax.get_yaxis().set_visible(False)
        if i != len(approx_coeffs)-1:
            ax.get_xaxis().set_visible(False)
        plt.text(-(len(y) - 1)*0.15, np.mean(y), "D%d" % (i + 1))

    # Display graph on screen
    plt.show()
    plt.close()
    
# own function added
def plot_4_graph(xs,ys, titles):
    plt.rcParams['figure.figsize'] = [10, 5]
    fig, axs = plt.subplots(2, 2)
    for i in range(2):
        for j in range(2):
            axs[i,j].plot(xs[i*2+j], ys[i*2+j])
            axs[i,j].set_title(titles[i*2+j])
    plt.show()
    
def plot_hist(ts, bins=60):
    plt.rcParams['figure.figsize'] = [20, 10]
    fig, axs = plt.subplots(2, 2)
    for i in range(2):
        axs[i,0].hist(np.abs(ts[i]), bins=bins)
        axs[i,1].hist(np.abs(ts[i]), bins=bins, cumulative=True, stacked=True, density=True)
    plt.show()