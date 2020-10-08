def triangles(n):
    L=[1]
    while len(L)<n:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
for t in triangles(10):
    print(t)
