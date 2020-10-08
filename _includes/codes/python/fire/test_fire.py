import fire 

a=5

def hello(name):
    return 'Hello {name}!'.format(name=name)

def hello1(name):
    return 'Hello1 {name}!'.format(name=name)

if __name__=='__main__':
    fire.Fire()
