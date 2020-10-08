def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michael',30)
person('Bob',25,city='Beijing')
extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)

