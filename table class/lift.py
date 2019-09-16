# 클래스 이름
class Lift:
    #생성자
    def __init__(self, current_floor=0):
        self.current_floor = current_floor

    #메서드(현재 층과 새로운 층으로 움직이는 층)
    def get_floor(self):
        return self.current_floor

    def move_to_floor(self, floor_number):
        self.current_floor = floor_number
