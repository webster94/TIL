from faker import Faker ## 설치한 faker모듈에서 Faker class를 데려옴
fake = Faker()  ## fake는 객체
print(fake.name())  ## name은 faker 의 instance method
fake_ko = Faker('ko_KR')
print(fake_ko.name())


import random
random.seed(7777)
print(random.random())
print(random.random())
random.seed(7777)    
print(random.random())
print(random.random())

#Fake.seed(4321)

fake= Faker('ko_KR') ## 변수를 클라스에 등록
Faker.seed(4321)
print(fake.name())
fake.ko =(Faker('ko_KR')) #페이크클라스 인자에 ko_kr 을 등록, fake.ko 메서드임!
print(fake_ko.name())

fake2 = Faker('ko_KR')
print(fake2.name())