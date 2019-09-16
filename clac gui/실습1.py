from tkinter import *
from decimal import *

#키 입력 함수:
def click(key):
    display.insert(END,key)

window = Tk()
window.title("MyCalculator")

top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

display = Entry(top_row, width=45, bg = "light green")
display.grid()

num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7','8','9',
'4','5','6',
'1','2','3',
'0','.','=' ]

r = 0
c = 0

for btn_text in num_pad_list:
    Button(num_pad, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# 연산자 프레임 생성
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
'*','/',
'+','-',
'(',')',
'C']

# 반복문으로 연산자 버튼 생성
r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

        
##### 메인 박복문 실행
window.mainloop()
