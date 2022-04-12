#HW:
# 1) Создать класс Person c атрибутами first_name, last_name
# 2) Создать доп.класс Jack и наследовать его от Person , добавив при этом дополнительные 
# атрибуты phone_number , balance 
# 3) Создать еще один класс Vito, который будет наследоваться от класса Jack :
# у последнего класса должен быть дополнительный 1 метод:
# первый метод,который минусует от balance Jack n-число и плюсует это число к 
# Vito.balance

# Отправить дз через GitHub

class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    def __init__(self, first_name, last_name,phone_number,balance):
        super().__init__(first_name, last_name)  
        self.phone_number = phone_number
        self.balance = balance



bema = Jack('Begimai','Akylbekova','0707232459',1000000)

class Vito(Jack):
    number = 790

    def extra(self):
        subtract = bema.balance - self.number
        addition = self.balance + subtract
        print(addition)

res=Vito('Begimai','akylbekova','0707232459',89 )

Vito.extra(res)        




