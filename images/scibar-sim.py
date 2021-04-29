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

x=np.loadtxt('scibar-sim.csv',delimiter=',',comments='#')
tns=x[0:75,1]
new=x[75:150,1]
old=x[150:,1]
t=np.arange(-1300,3200,60)
c=sns.color_palette('deep')
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ax.plot(t,tns,ds='steps-mid')
ax.plot(t,old,ds='steps-mid')
ax.plot(t,new,ds='steps-mid')
ax.set_xlim(-1000,3000)
ax.set_ylim(6.2e4,7.4e4)
ax.axvline(x=0,color='black',ls=':')
ax.set_xlabel(r'Tiempo $\left[\si{\second}\right]$',x=0.9,ha='right')
ax.set_ylabel(r'Cuentas TNS $\left[\si{\per\minute}\right]$')
plt.tight_layout(pad=1.0)
plt.savefig('scibar-sim.pdf')
plt.show()
