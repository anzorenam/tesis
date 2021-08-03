#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')

f=open('absp.txt','r')
a=f.readlines()
f.close()
ebins=np.arange(300,700,10)
abs=np.zeros(22153)
k=0
for elem in a:
  abs[k]=float(elem.split()[4])
  k+=1

f=open('emit.txt','r')
a=f.readlines()
f.close()
emi=np.zeros(101219)
k=0
for elem in a:
  emi[k]=float(elem.split()[3])
  k+=1

c=sns.color_palette('deep')
sns.set_palette(c)
fig,ax=plt.subplots(nrows=1,ncols=1)
ax.hist(abs,bins=ebins,histtype='stepfilled',alpha=0.6)
ax.hist(emi,bins=ebins,histtype='stepfilled',alpha=0.6)
ax.set_yscale('log')
ax.set_ylim(1e0,1e5)
ax.set_xlim(300,700)
plt.xlabel(r'$\lambda \left[\si{\nano\metre}\right]$',x=0.9,ha='right')
plt.ylabel(r'$\log_{10}\left(\text{Cuentas}\right)$')
plt.tight_layout(pad=1.0)
plt.savefig('sim-optics-spect.pdf')
plt.show()
