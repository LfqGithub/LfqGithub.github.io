import numpy as np
import matplotlib.pyplot as plt 

def s_sin(ax):
    x=np.linspace(0,2*np.pi,100)
    ax.plot(x, np.sin(x))
    ax.set_xlabel('x')
    ax.set_ylabel('y=sin(x)')
    return ax
def d_sin(ax):
    x=np.linspace(0,4*np.pi,100)
    ax.plot(x, np.sin(x))
    ax.set_xlabel('x')
    ax.set_ylabel('y=sin(x)')
    return ax
def s_cos(ax):
    x=np.linspace(0,2*np.pi,100)
    ax.plot(x, np.cos(x))
    ax.set_xlabel('x')
    ax.set_ylabel('y=cos(x)')
    return ax
def d_cos(ax):
    x=np.linspace(0,4*np.pi,100)
    ax.plot(x, np.cos(x))
    ax.set_xlabel('x')
    ax.set_ylabel('y=cos(x)')
    return ax
def sin_and_cos():
    ax1=plt.subplot2grid((3,2),(0,0))
    s_sin(ax1)
    ax2=plt.subplot2grid((3,2),(0,1))
    s_cos(ax2)
    ax3=plt.subplot2grid((3,2),(1,0), colspan=2)
    d_sin(ax3)
    ax4=plt.subplot2grid((3,2),(2,0), colspan=2)
    d_cos(ax4)

    plt.tight_layout()
    plt.savefig('multi-figures-control.png',dpi=300)
    #plt.show()

def single_figure():
    ax=plt.subplot2grid((1,1),(0,0))
    s_sin(ax)
    plt.tight_layout()
    plt.savefig('output-put-single-subplot.png',dpi=300)
    #plt.show()

def main():
    single_figure()
    plt.figure(0)
    sin_and_cos()

if __name__ == '__main__':
    main()
