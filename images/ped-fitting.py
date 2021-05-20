#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optim
import scipy.signal as signal
import seaborn as sns
import argparse
import os

def parabola(x,k,m,c):
  return k-c*np.square(x-m)

def fits(log_data,bins,N,M):
  amax=np.argmax(log_data,axis=1)
  nchs=np.arange(0,N)
  nfits=0
  pdata=np.zeros([2,N])
  for nch in nchs:
    xdata=np.arange(amax[nch]-4,amax[nch]+5+1)
    ydata=log_data[nch,xdata]
    if np.all(ydata):
      popt,pcov=optim.curve_fit(parabola,xdata,ydata)
      perr=np.sqrt(np.diag(pcov))
      if np.all(perr<1.0):
        ds=np.sqrt(1.0/(2.0*popt[2]*np.log(10.0)))
        pdata[0,nch]=np.uint16(np.rint(popt[1]))
        pdata[1,nch]=ds
        nfits+=1
  return pdata[0,:],pdata[1,:],nfits

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')

parser=argparse.ArgumentParser()
parser.add_argument('nbeb', help='beb num',type=int)
parser.add_argument('plot', help='plot',type=int)

args=parser.parse_args()
nbeb=args.nbeb
plot=args.plot

name='adc-cped20_171114.dat'
x=np.loadtxt(name)

xlog=np.log10(x,where=x>0)
N=256
Mbins=4096
y=xlog
bins=np.arange(0,Mbins)

ped_m,ped_sigma,nfits=fits(y,bins,N,Mbins)

if plot==True:
  j=1
  c=sns.color_palette('dark')
  for k in range(0,1):
    fig,ax=plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)
    ax.plot(bins-ped_m[j],y[j,:],drawstyle='steps-mid',color=c[7])
    ax.fill_between(bins-ped_m[j],y[j,:],0,alpha=0.5,step='mid',color=c[7])
    ax.axvline(x=0,color=c[7])
    plt.xlabel(r'Canal ADC',x=0.9,ha='right')
    plt.ylabel(r'$\log_{10}\left(\si{Cuentas}\right)$')
    plt.xlim(-50,400)
    plt.ylim(0,6)
  plt.tight_layout(pad=1.0)
  plt.savefig('neutron-ped.pdf')
  plt.show()
