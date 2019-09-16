from tkinter import*

class Table :
    ### 생성자
    def __init__(self,window,colour = "black"
                 , net_colour = 'green'
                 , width = 600
                 , height = 400
                 , vertical_net = False
                 , horizontal_net = False):
        self.width = width
        self.height = height
        self.colour = colour
    # tkinter 공장으로부터 캔버스 주문:
        self.canvas = Canvas(window
                            , bg=self.colour
                            , height=self.height
                            , width = self.width)
        self.canvas.pack()
        
    
    
