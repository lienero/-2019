a=20

def func(a):
    print('a는 ', a)
    a=10
    print('로컬변수 a는', a)

func(a)
print(a)
