# MyPong의 주된 파일을 만듭니다.
from tkinter import *
import table2


# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("My Table Experiment")
       
# Table 공장으로부터 table 주문
my_table = table2.Table(window
                       , net_colour = "green"
                       , vertical_net=True)        

# GUI를 계속 그리는 반복문 시작
window.mainloop()                       

