a=20

def func(b):
    print('b는 ', b)
    global a
    a=10
    print('로컬변수 a는', a)

func(a)
print(a)
