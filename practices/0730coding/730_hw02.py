class Dog:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

dog = Dog('멍멍이')
dog.walk()
dog.eat()
class Bird:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')
bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
