#키 입력 함수:
def click(key):
    #= 버튼이 눌렸을 때 계산 수행:
    if key == "=":
        result = str(eval(display.get()))
        display.insert(END, "=" + result)
    #C 버튼이 눌려졌을 때 display 엔트리 위젯 내용 비움:
    elif key == "C":
        display.delete(0,END)

        
    # 그 외 다른 키를 눌렀을 때 실행될 기본 동작:
    else:
        display.insert(END,key)
