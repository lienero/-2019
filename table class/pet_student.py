#클래스 이름
class Pet:

# 생성자
    def __init__ (self, name):
        self.name = name


#메서드완성(sleep)
    def sleep(self):
        print(self.name , '가 잠을 잡니다.')

#메서드완성(eat)
    def eat(self):
        print(self.name, '가 약간의 음식을 먹습니다.')
        print(self.name, '가 조금 더 음식을 원합니다')
        
