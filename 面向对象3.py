# 面向对象3的后续部分
class Car:
    speed = 0
    def drive(self,distance):
        time = distance/self.speed
        print(time)  # return float(time)
        a=time
car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
print('car1 costs time: %,6f%a)

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)
