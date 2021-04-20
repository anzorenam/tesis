#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')
mat.rc('text',usetex=True)
mat.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[spanish]{babel}\usepackage{mathpazo}\usepackage[euler-digits,euler-hat-accent]{eulervm}\usepackage{amsmath,amsfonts,amssymb}\usepackage{siunitx}')

c=299792458.0
R=1.495978707e11
nm=939.56542052
tau=880.3
Ek=np.arange(10,1000,10)
gamma=Ek/nm+1
beta=np.sqrt(1.0-(1.0/gamma**2.0))
tflight=R/(c*beta)
p=np.exp(-1.0*tflight/(gamma*tau))
c=sns.color_palette('deep')
fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False)
ax[0].loglog(Ek,p,color=c[0])
ax[0].set_xlim(1e1,1e3)
ax[0].set_ylim(1e-2,1e0)
ax[0].set_xlabel(r'Energía cinética $\left[\si{\mega\electronvolt}\right]$',x=0.9,ha='right')
ax[0].set_ylabel(r'$P\left(E_{k},1AU\right)$')
ax[1].semilogx(Ek,tflight/60.0,color=c[1])
ax[1].set_xlim(1e1,1e3)
ax[1].set_ylim(0,60)
ax[1].set_xlabel(r'Energía cinética $\left[\si{\mega\electronvolt}\right]$',x=0.9,ha='right')
ax[1].set_ylabel(r'Tiempo vuelo $\left[\si{\minute}\right]$')
plt.tight_layout(pad=1.0)
plt.savefig('neutron-prob.pdf')
plt.show()
