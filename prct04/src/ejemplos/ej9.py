import matplotlib.pylab as pl 
import numpy as np

pl.figure(figsize=(8,6), dpi=80)

pl.subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(X)
S = np.sin(X)

pl.plot(X,C, color="blue", linewidth=2.5, linestyle="-", label="coseno")
pl.plot(X,S, color="red", linewidth=2.5, linestyle="-", label="seno")

pl.legend(loc='upper left')

#pl.xlim(-4.0,4.0)
pl.xlim(X.min()*1.1,X.max()*1.1)

#pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$']
          )

#pl.ylim(-1.0,1.0)
pl.ylim(C.min()*1.1,C.max()*1.1)

#pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$']
         )

pl.savefig("sencos.eps", dpi=72)

pl.show()
