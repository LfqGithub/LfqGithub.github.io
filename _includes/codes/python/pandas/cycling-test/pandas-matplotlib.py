import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price=pd.Series(np.random.randn(150).cumsum(), index=pd.date_range('2000-1-1',periods=150,freq='B'))
ma=price.rolling(20).mean()
mstd=price.rolling(20).std()
plt.figure()
plt.plot(price.index,price,'k')
plt.plot(ma.index,ma,'b')
plt.fill_between(mstd.index,ma-2*mstd,ma+2*mstd,color='b',alpha=0.2)
plt.show()
