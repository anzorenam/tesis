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

x=np.loadtxt('scibar-edep.csv',delimiter=' ')
ebins=np.arange(100,20000,150)
c=sns.color_palette('deep')
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ax.hist(x[:,1],bins=ebins,log=True,histtype='stepfilled',color='black',alpha=0.8)
ax.set_xlim(100,20000)
ax.set_ylim(1e0,1e3)
ax.axvline(x=0,color='black',ls=':')
ax.set_xlabel(r'Energía $\left[\si{\mega\electronvolt}\right]$',x=0.9,ha='right')
ax.set_ylabel(r'$\log_{10}(\text{Cuentas})$')
plt.tight_layout(pad=1.0)
plt.savefig('scibar-edep.pdf')
plt.show()
