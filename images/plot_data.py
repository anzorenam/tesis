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
mat.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[spanish]{babel}\usepackage{mathpazo}\usepackage[euler-digits,euler-hat-accent]{eulervm}\usepackage{amsmath,amsfonts,amssymb}\usepackage{siunitx}')

qe=1.602176634
c=0.299792458
h=6.62607015
Kconv=h*(1.0/qe)*c*(1e3)
data0=np.loadtxt('scibar_optics0.csv')
data1=np.loadtxt('scibar_optics1.csv')
lamb=Kconv/data0[0,:]
ps_emi=data0[4,:]
wls_abs=data0[7,:]
wls_emi=data0[5,:]

c0=sns.husl_palette(10,l=.5,s=0.5)
fig,ax0=plt.subplots(nrows=1,ncols=1)
f0=ax0.plot(lamb,ps_emi,color=c0[7],label='Sci-emi')
f1=ax0.plot(lamb,wls_emi,color=c0[4],label='WLS-emi')
ax0.set_ylabel('Unidades arbitrarias')
ax0.set_xlabel(r'$\lambda \left[\si{\nano\metre}\right]$',x=0.9,ha='right')
ax1=ax0.twinx()
f2=ax1.semilogy(lamb,wls_abs,color=c0[0],label='WLS-abs')
ax1.set_ylabel(r'Longitud de atenuación $\left[\si{\mm}\right]$')
ft=f0+f1+f2
labs=[f.get_label() for f in ft]
ax0.legend(ft,labs,loc=1)
plt.xlim(300.0,800.0)
plt.ylim(1e-1,1e4)
plt.tight_layout(pad=1.0)
plt.savefig('scibar-optics.pdf',bbox_inches='tight')
plt.show()
