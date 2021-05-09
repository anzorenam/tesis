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

a=np.arange(0,89)
adist=np.loadtxt('angular-dist.dat',delimiter=' ',comments='#')
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ax.plot(a,adist[0,:],ds='steps-mid')
plt.show()
