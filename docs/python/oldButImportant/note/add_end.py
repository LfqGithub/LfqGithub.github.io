def add_end(L=[]): # 默认参数必须为不可变对象，否则多次调用后会出现不同的结果
    L.append('end')
    return L
def add_end1(L=None):# 不可变对象
    if L is None:
        L=[]
    L.append('end')
    return L


