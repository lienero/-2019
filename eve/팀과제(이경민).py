
#tkinter, random 삽입

from tkinter import *
import random


# 키 입력 함수:

def click(key):
    #변수 선언 및 칸 비우기
    Evolution = list(my_glossary.keys())
    display.delete(0, END)
    output.delete(0.0, END)

    # 버튼이 눌렸을 때 계산 수행:

    # 랜덤함수를 이용한 랜덤 지정
    if key == "랜덤진화":
        display.insert(END, random.choice(Evolution))
        if display.get() == "이브이" :
            
            eevee = PhotoImage(file = "EVE1.png")    

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

        elif display.get() == "부스터" :
            eevee = PhotoImage(file = "BST1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

        elif display.get() == "샤미드" :
            eevee = PhotoImage(file = "SMID1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)        
        elif display.get() == "쥬피썬더" :
            eevee = PhotoImage(file = "JYP1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)        
        elif display.get() == "에브이" :
            eevee = PhotoImage(file = "AV1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
        elif display.get() == "블래키" :
            eevee = PhotoImage(file = "BL1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)            
        elif display.get() == "님피아" :
            eevee = PhotoImage(file = "NP1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

        elif display.get() == "글레이시아" :
            eevee = PhotoImage(file = "GL1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

        elif display.get() == "리피아" :
            eevee = PhotoImage(file = "LP1.png")

            eve_label = Label(image = eevee)
            eve_label.image = eevee
            eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
        
    # C 버튼이 눌려졌을 때 진화 캔슬:           
    elif key == "C":
        display.insert(END, "이브이")
        eevee = PhotoImage(file = "EVE1.png")    

        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
    # 버튼 별 이미지 및 텍스트 지정  
    elif key == "불의 돌":
        display.insert(END, "부스터")
        eevee = PhotoImage(file = "BST1.png")
        
        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

    elif key == "물의 돌":
        display.insert(END, "샤미드")
        eevee = PhotoImage(file = "SMID1.png")    

        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

    elif key == "천둥의 돌":
        display.insert(END, "쥬피썬더")
        eevee = PhotoImage(file = "JYP1.png")    

        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
    elif key == "낮":
        display.insert(END, "에브이")
        eevee = PhotoImage(file = "AV1.png")    

        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
    elif key == "밤":
        display.insert(END, "블래키")
        eevee = PhotoImage(file = "BL1.png")    

        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
    elif key == "페어리":
        display.insert(END, "님피아")
        eevee = PhotoImage(file = "NP1.png")    

        eve_label = Label(image = eevee)
        eve_label.image = eevee
        eve_label.grid(row=0, column=0, columnspan=1, sticky=E)
    #엔트리에 나타난 텍스트 회수 및 사전 불러오기
    display_text = display.get()
    definition = my_glossary[display_text]
    output.insert(END,definition)

        

##### 메인:
window = Tk()
window.title("이브이 진화 시뮬레이터")

#레이블 생성
Label(window, text="버튼을 눌러 진화를 해보세요 :").grid(row=0, column=0, sticky=W)

# top_row 프레임 생성
top_row = Frame(window)
top_row.grid(row=1, column=0, columnspan=2, sticky=W)

# 수정 가능한 엔트리 위젯
display = Entry(top_row, width=45, bg="light green")
display.grid()


# 진화 프레임 생성
operator = Frame(window)
operator.grid(row=3, column=1, sticky=E)

operator_list = [
'불의 돌', '물의 돌',  
'천둥의 돌', '낮',
'밤', '페어리',
'C', '랜덤진화' ]

# 반복문으로 진화 버튼 생성
r = 1
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text, width=10, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1


# 다른 레이블 생성
Label(window, text="\n도감:").grid(row=2, column=0, sticky=W)

# 텍스트 박스 생성
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=3, column=0, columnspan=1, sticky=W)

# 사전:
my_glossary = {
    '이브이': '다양한 모습으로 진화한다. 이브이의 유전자는 진화의 비밀을 밝혀낼 열쇠다.' ,
    '부스터': '흥분하면 체내에 있는 불꽃 주머니에 불이 붙어서 체온이 900도까지 오른다.',
    '샤미드': '아름다운 물가가 주요 서식지다. 외적에게 습격당할 상황이 되면 물로 뛰어들어 모습을 감춘다.',
    '쥬피썬더': '곤두세운 털을 바늘처럼 날린다. 적이 약해진 순간 1만 볼트의 전격으로 처리한다.',
    '에브이' : '원래는 아무런 능력도 없었지만 몸을 지키기 위해 예지 능력에 눈뜨게 됐다고 한다.',
    '블래키' : '어둠 속에 숨어 먹이를 노린다. 습격하는 순간 몸의 둥근 무늬가 희미하고 이상하게 빛난다.',
    '님피아' : '트레이너의 팔에 리본 모양의 더듬이를 휘감는다. 닿으면 기분을 알 수 있기 때문이다.',
    '글레이시아' : '몸의 털을 얼려 예리한 바늘로 만들어 몸을 지킨다. 체온은 마이너스 60도까지 내릴 수 있다.',
    '리피아' : '다툼을 좋아하지 않지만 동료를 지키기 위해서라면 꼬리의 잎사귀를 날카로운 칼날로 만들어 싸운다.',
    }

#기본
display.insert(END, "이브이")

eevee = PhotoImage(file = "EVE1.png")

eve_label = Label(image = eevee)
eve_label.image = eevee
eve_label.grid(row=0, column=0, columnspan=1, sticky=E)

display_text = display.get()
definition = my_glossary[display_text]
output.insert(END,definition)


##### 메인 반복문 실행
window.mainloop()

