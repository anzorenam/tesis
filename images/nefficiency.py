#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integral
import scipy.stats as stats
import seaborn as sns

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')
plt.rc('text',usetex=True)
plt.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc} \usepackage[T1]{fontenc} \usepackage[spanish]{babel} \usepackage{mathpazo}\usepackage[euler-digits,euler-hat-accent]{eulervm} \usepackage{amsmath,amsfonts,amssymb} \usepackage{siunitx}')

atot=2.0*np.pi*280**2.0
wilson=True
c0=sns.color_palette('deep')
m=[1,1.2,1.6]
#sns.cubehelix_palette(8,rot=-.4,reverse=True)
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
for k in range(0,3):
  dEff=np.loadtxt('neutron-deff-{0}.dat'.format(k))
  p,x,n=dEff[0,:],dEff[0,:]*dEff[1,:],dEff[1,:]
  if wilson==False:
    pH,pL=stats.beta.ppf(1-0.025,x+1,n-x),stats.beta.ppf(0.025,x,n-x+1)
  else:
    pL=(2.0*x+1.96**2.0-(1.96*np.sqrt(1.96**2.0-(1.0/n)+4.0*x*(1.0-p)+(4.0*p-2.0))+1.0))/(2.0*(n+1.96**2.0))
    pH=(2.0*x+1.96**2.0+(1.96*np.sqrt(1.96**2.0-(1.0/n)+4.0*x*(1.0-p)-(4.0*p-2.0))+1.0))/(2.0*(n+1.96**2.0))
  ebins=np.ravel(np.outer(10**np.arange(1,5),np.arange(1,10)))
  ax.errorbar(ebins[0:28],m[k]*p,yerr=(p-pL,pH-p))
  ax.set_xscale('log')
  ax.set_yscale('log')
plt.xlabel(r'Energía $[\si{\mega\electronvolt}]$',x=0.9,horizontalalignment='right')
plt.ylabel(r'Eficiencia de detección')
plt.xlim(5e0,1e4)
plt.ylim(1e-5,1e0)
plt.tight_layout(pad=1.0)
plt.savefig('electronics-deff.pdf')
plt.show()
