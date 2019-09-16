#myGlossary_start.py

from tkinter import *

#키 입력 함수:
def click():
    entered_text = entry.get()
    output.delete(0.0, END)
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "단어의 정의를 찾을 수 없습니다."
    output.insert(END,definition)

##### 메인:
window = Tk()
window.title("My coding Club Glossary")

#레이블 생성
Label(window, text="정의되어 있는 단어를 입력하고 엔터 키를 누르세요:").grid(row=0, column=0, sticky=W)

#텍스트 앤트리 위젯 생성
entry = Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, sticky=W)


#제출 버튼 추가
Button(window, text="제출", width=5, command=click).grid(row=2,column=0,sticky=W)


#다른 레이블 생성
Label(window, text="\n정의:").grid(row=3, column=0, sticky=W)

#텍스트 박스 생성
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

#사전
my_glossary= {
    '알고리즘': '컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할수 있도록 단계별로 설명해놓은 것',
    '버그': '프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각',
    '2진수':'2전법으로 나타낸 숫자'
    }
##### 메인 반복문 실행
window.mainloop()
