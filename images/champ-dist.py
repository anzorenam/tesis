#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')

adc_bins=np.arange(0,500.5,0.5)
adc_max0=np.loadtxt('adc-max-171114.dat0')
Ntot=np.sum(adc_max0)
fig,ax=plt.subplots(nrows=1,ncols=2)
mthr=0
Nhit=0
for j in range(0,28):
  mthr+=adc_bins[np.argwhere(adc_max0[j,:])[0][0]]
  Nhit+=np.sum(adc_max0[j,:]<7.0)
  adc_sum=np.cumsum(adc_max0[j,:])/np.sum(adc_max0[j,:])
  ax[1].plot(adc_bins,adc_sum,ds='steps-mid')
  ax[1].set_yscale('log')
  ax[1].set_xlim(0,30.0)
  ax[1].set_ylim(1e-4,1.1e0)
  ax[1].set_xlabel(r'Energía $\left[\si{\mega\electronvolt}\right]$',x=0.9,ha='right')
  ax[1].set_ylabel(r'Fracción de eventos')
  ax[0].plot(adc_bins,adc_max0[j,:],ds='steps-mid')
  ax[0].set_yscale('log')
  ax[0].set_xlim(0,100.0)
  ax[0].set_ylim(1e0,2e3)
  ax[0].set_xlabel(r'Energía $\left[\si{\mega\electronvolt}\right]$',x=0.9,ha='right')
  ax[0].set_ylabel(r'$\log_{10}(\text{Cuentas})$')

plt.tight_layout(pad=1.0)
plt.savefig('scibar-threshold.pdf')
plt.show()

print(mthr/28.0,Nhit/Ntot)
