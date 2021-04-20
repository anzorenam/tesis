#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')
mat.rc('text',usetex=True)
mat.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[english]{babel}\usepackage{mathpazo}\usepackage[euler-digits,euler-hat-accent]{eulervm}\usepackage{amsmath,amsfonts,amssymb}\usepackage{siunitx}')

ebins=np.arange(10.0,2000.0,1.0)
n=np.loadtxt('neutron_attenuation.dat')
norm=n/np.amax(n)
Ntot=np.sum(n,axis=1)/1e8
c0=sns.cubehelix_palette(10,start=0.2,rot=-.3,dark=0.1,reverse=True)
sns.set_palette(c0)
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ax.semilogy(ebins,np.transpose(norm)*Ntot)
ax.set_xlabel(r'Energía cinética $\left[\si{\mega\electronvolt}\right]$',x=0.9,ha='right')
ax.set_ylabel(r'Atenuación')
ax.set_xlim(5e1,1.5e3)
ax.set_ylim(1e-6,1e0)
plt.tight_layout(pad=1.0)
plt.savefig('neutron-at.pdf')
plt.show()
