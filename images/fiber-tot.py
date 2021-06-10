#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import time
import argparse
import scipy.stats as stats
import scipy.signal as signal
import seaborn as sns

sns.set(rc={"figure.figsize":(12,6)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.0})
sns.set_style('ticks')
mat.rc('text',usetex=True)
mat.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[english]{babel}\usepackage{mathpazo}\usepackage[euler-digits,euler-hat-accent]{eulervm}\usepackage{amsmath,amsfonts,amssymb}\usepackage{siunitx}')

parser=argparse.ArgumentParser()
parser.add_argument('allplot', help='muestra resultado de la simulacion',type=int)

args=parser.parse_args()
plot_all=args.allplot
t0=time.time()

tau=40.0 # peaking time n*tau
step=0.1
n=2.0 # semi-gaussian shaper 1 dif + 2 int
thrs_adc=2110.0
tot_t=120.0
m_fit,b_fit=800.0,2100.0
pt=n*tau
N=500
M=10000

t=np.arange(0,N,step)
thrs=(1.0/m_fit)*(thrs_adc-b_fit)
eadc=stats.norm.rvs(loc=2400,scale=72.0,size=M)
evolt=(1.0/m_fit)*(eadc-b_fit)
etime=np.power(t/tau,n)*np.exp(-t/tau)
eout=(1.0/np.amax(etime))*etime*np.transpose(evolt[np.newaxis])
etot=step*np.sum(eout>thrs,1)

if plot_all==True:
  c=sns.color_palette('deep')
  sns.set_palette(c)
  fig=plt.figure()
  ax=fig.add_subplot(2,2,1)
  ax.plot(t,np.transpose(1000.0*eout[0:25,:]))
  plt.xlabel(r'Tiempo $\mathrm{\left[\si{\nano\second}\right]}$',x=0.95,horizontalalignment='right')
  plt.ylabel(r'Amplitud $\mathrm{\left[\si{\milli\volt}\right]}$')
  plt.ylim(0,600)
  ax=fig.add_subplot(2,2,3)
  bins=np.arange(2000,3000,10)
  n,bins,patches=ax.hist(eadc,bins=bins,histtype='stepfilled',facecolor='0.15',edgecolor='0.28')
  plt.xlabel(r'canal ADC')
  plt.ylabel(r'Cuentas')
  plt.xlim(2000,2800)
  ax=fig.add_subplot(2,2,2)
  ax.scatter(evolt,etot,s=5)
  plt.xlabel(r'Amplitud $\mathrm{\left[\si{\milli\volt}\right]}$')
  plt.ylabel(r'TOT $\mathrm{\left[\si{\nano\second}\right]}$')
  ax=fig.add_subplot(2,2,4)
  bins=np.arange(200,400,2)
  n,bins,patches=ax.hist(etot,bins=bins,histtype='stepfilled',facecolor='0.15',edgecolor='0.28')
  plt.xlabel(r'TOT $\mathrm{\left[\si{\nano\second}\right]}$')
  plt.ylabel(r'Cuentas')
  plt.xlim(240,380)
  plt.tight_layout(pad=1.0)
  plt.savefig('TOT-model.pdf')
  plt.show()
