import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
import mpltex
import numpy as np

@mpltex.presentation_decorator
def testPlotSin():
    x=np.linspace(0,6,100)
    y=np.sin(x)
    print(y)
    fig,ax=plt.subplots(1)
    plt.plot(x,y)
    plt.tight_layout(pad=0.1)
    #fig.savefig('testPlotSin.png')
    plt.show()

if __name__=='__main__':
    testPlotSin()
