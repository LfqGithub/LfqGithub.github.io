import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
ts=ts.cumsum()
#plt.figure()
#ts.plot()

df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list('ABCD'))
df=df.cumsum()

#df.plot()

df3=pd.DataFrame(np.random.randn(1000,2),columns=['B','C']).cumsum()
df3['A']=pd.Series(list(range(len(df3))))
#df3.plot(x='A',y='B')

df2=pd.DataFrame(np.random.randn(10,4),columns=list('ABCD'))
# df2.plot.barh(stacked=True)


#df.iloc[5].plot(kind='bar')

df4=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000), 'c':np.random.randn(1000)-1},columns=list('abc'))

#df4.plot.hist(alpha=0.5)
#df4.plot.hist(stacked=True, bins=20)
#df.diff().hist(color='k',alpha=0.5,bins=50)

data=pd.Series(np.random.randn(1000))
#data.hist(by=np.random.randint(0,4,1000))
#data.hist()

df=pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
#df.plot.box()


df5=pd.DataFrame(np.random.rand(10,2),columns=['Col1','Col2'])
df5['X']=pd.Series(['A','A','A','A','A','B','B','B','B','B'])
df5.plot.box(by='X')



plt.savefig('test.png',dpi=300)
