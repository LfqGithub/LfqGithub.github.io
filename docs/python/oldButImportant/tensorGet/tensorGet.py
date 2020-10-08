import numpy as np 
from scipy import io
from sympy import *
import scipy.io as sio
import sys

class getTensor():
    def __init__(self,lambdamax,theta,v11,v21):
        print(' \n  Four command line parameters are required : lambda_max, theta(^o), v11,v21')
        self.lambdamax=float(sys.argv[1]) # the max eigenvalue of the tensor \lambda_{max}
        self.theta=int(sys.argv[2])/180*np.pi # the tilt angle of rod chains
        self.v11=float(sys.argv[3]) # the related eigenvector of eigenvalue ,v(i,:) is corresponding to \lambda_{i} 
        self.v21=float(sys.argv[4])
        self.vec=np.empty([3,3])
        self.lambdaAll=np.diag((self.lambdamax,-0.5*self.lambdamax,-0.5*self.lambdamax))
        print('\n','lambda_max= ',self.lambdamax,'\n')
        print(' theta= ',np.around(self.theta,4),'\n')
        print(' v11= ',self.v11,'\n')
        print(' v21= ',self.v21,'\n')
    def vMaxGet(self):
        v12,v13=symbols("v12 v13")
        ans1=solve([self.v11**2+v12**2+v13**2-1,sqrt(self.v11**2+v12**2)/v13-tan(self.theta)],[v12,v13],tuple=True)
        return ans1[0] # the equations may have many solutions, we just take the first one
    def vGet(self,ans1):
        v22,v23,v31,v32,v33=symbols("v22,v23,v31,v32,v33")
        # v_1 is perpendicular to v_2 and v_3, both vectors are unit vector
        ans2=solve([self.v11*self.v21+ans1[0]*v22+ans1[1]*v23,self.v11*v31+ans1[0]*v32+ans1[1]*v33,self.v21*v31+v22*v32+v23*v33,self.v21**2+v22**2+v23**2-1,v31**2+v32**2+v33**2-1],[v22,v23,v31,v32,v33],tuple=True)
        return ans2[0]
    def getTau(self,ans1,ans2):
        vector9=(self.v11,ans1[0],ans1[1],self.v21,ans2[0],ans2[1],ans2[2],ans2[3],ans2[4])
        vector=np.around(np.asarray(vector9).reshape((3,3)).astype(np.double),4)
        vec=vector.T
        self.vec=vec
        print(' vec is \n', vec)
        invVec=np.linalg.inv(vec)
        lambdaAll=np.diag((self.lambdamax,-0.5*self.lambdamax,-0.5*self.lambdamax))
        Tau=np.around(np.dot(np.dot(vec,lambdaAll),np.linalg.inv(vec)),4) # A*B in matlab is equal to np.dot(A,B) in python
        print(' lambda is \n \n ',lambdaAll)
        return Tau
    def getTauInCalc(self,Tau):
        TauFinal=np.empty([6,256])
        for i in range(256):
            TauFinal[0,i]=Tau[0,0]
            TauFinal[1,i]=Tau[1,1]
            TauFinal[2,i]=Tau[2,2]
            TauFinal[3,i]=Tau[1,0]
            TauFinal[4,i]=Tau[2,0]
            TauFinal[5,i]=Tau[1,2]
        result=np.asarray(TauFinal)
        return result
    def debug(self,Tau9):
        lam,ve=np.linalg.eig(Tau9)
        print('\n  lambdaVerfy is  \n \n',np.around(lam,4))
        print('\n  vectorVerfy is  \n \n ',np.around(ve,4))

            




b=getTensor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
ans1=b.vMaxGet()
ans2=b.vGet(ans1)
Tau9=b.getTau(ans1,ans2)
b.debug(Tau9)
Tau=b.getTauInCalc(Tau9)
# four parameters: lambda, angle, v11,v21
name='angle'+str(sys.argv[2])+'Lambda'+str(b.lambdamax)+'V11_'+str(b.v11)+'V21_'+str(b.v21)+'.mat'
sio.savemat(name,{'Tau':Tau,'angle':int(sys.argv[2]),'v11':b.v11,'v21':b.v21,'lambda':b.lambdamax})



