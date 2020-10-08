import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,400)
y=np.sin(x**2)
plt.close('all')
#f,ax=plt.subplots()
#ax.plot(x,y)
#ax.set_title('simplt plot')

#f,axarr=plt.subplots(2,sharex=True)
#axarr[0].plot(x,y)
#axarr[0].set_title('sharing x axis')
#axarr[1].scatter(x,y)

#f,(ax1,ax2)=plt.subplots(1,2,sharey=True)
#ax1.plot(x,y)
#ax1.set_title('sharing y axis')
#ax2.scatter(x,y)

#f,(ax1,ax2,ax3)=plt.subplots(3,sharex=True,sharey=True)
#ax1.plot(x,y)
#ax1.set_title('sharing both axis')
#ax2.scatter(x,y)
#ax3.scatter(x,2*y**2-1,color='r')
#f.subplots_adjust(hspace=0) # the amount of height reserved for white space between subplots, expressed as a fraction of the average axis height
#plt.setp([a.get_xticklabels() for a in f.axes], visible=False)

f,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,sharex='col',sharey='row')
ax1.plot(x,y,x,y+2)
ax1.set_title('sharing x per column, y per row')
ax2.scatter(x,y)
ax3.scatter(x,2*y**2-1, color='r')
ax4.plot(x,2*y**2-1,color='r')











plt.show()

