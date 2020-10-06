![image-20201005102304787](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005102304787.png)

00 project

가상환경 키고

requirements.txt를 받는다.

migrate 실시!



django seed 사용법참고



command 창에

python manage.py seed articles --number = 20

이러면 난수 20개가 발생된다.



> 웹 검사기 >> NETWORL > HEADERS에html 문서라는 것을 확인가능하다.

이제 html문서로 응답안할 것이다.

응답은 

![image-20201005105655885](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005105655885.png)

Json Response

django core serializing



![image-20201005110536894](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005110536894.png)

![image-20201005110546022](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005110546022.png)

url>>

path('json_2/', views.article_list_json_2)

![image-20201005110908118](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005110908118.png)

![image-20201005111235091](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005111235091.png)



django rest framework 를 사용

json을 응답할건데, drf 로 만들어서 응답할 것이다.

![image-20201005111556087](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005111556087.png)

> 설치!



articles/ serializers.py 생성![image-20201005112211432](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112211432.png)

![image-20201005112114534](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112114534.png)

![image-20201005112219387](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112219387.png)

![image-20201005112151830](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112151830.png)

![image-20201005112328707](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112328707.png)

![image-20201005112652647](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112652647.png)

![image-20201005112916628](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005112916628.png)

json_1은 articles_jason의 인스턴스에 dictionary의 값들을 지정해서 받아온 것이고

json_2는 serializers.serialize를 활용해서 주소를 직렬화해서 가져온 것이고

json_3는 json_2를 serializers의 모델을 통해서 ...데이터를 정렬해줬다....라고생각하면될까요?

json3를 어떻게 해줬다고 설명해야할지 알려주실수있나용?



---

오후

reqirements.txt.까지 가상환경에 완료시킨다.

1.

![image-20201005141749480](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005141749480.png)

2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py seed articles --number=20

기본적인 완성이 되었다.



python manage.py shell_plus

우리가 정의한 모델들을 편하게 가져올 수 있따.django-extensions를 깐다



from articles seriallizers import Articleserializer



Article Serializer()

id와 필드들 그리고 필드들이 나올 것이다

Article.objects.get(pk=1)

article = Article.objects.get(pk=1)

serializer = ArticleSerializer(article)

serializer.data



![image-20201005143303634](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005143303634.png)

url 끝 , templates를 사용하지않는다.



![image-20201005144326235](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005144326235.png)

> 뷰함수

 

디테일!

![image-20201005144400724](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005144400724.png)

> urls

![image-20201005144654145](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005144654145.png)

> views

![image-20201005145016104](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005145016104.png)

serializer에 값추가

list로 이름변경!

![image-20201005145040598](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005145040598.png)

3.create

![image-20201005150455788](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005150455788.png)

postman 다운

----------------

rest 는 method(행위) , url(자원)

구상을 잘해야한다.

rest _ api에 대해서는 방식에 따라서 수정,삭제,create, detail이 가능하다.



겟방식일 땐다 가져와야함

articles 는 쿼리셋 형태임

serilaze는 파이썬에서 활용할 수 있게 바꿔줌

serializers.py 생성

from rest_framework import serializers

from .models import Article

class ArticleListserializer(serializers, ModelSerializer):

​	class Meta:

model = Article

fields = ('id','title',)

from .serializers import ArticleListSerializer

if request.method == 'GET':

articles = Article.objects.all()

erializer = ArticleListSerializer(articles, many = True) 리스트일경우에 이걸 적어야 넘어간다.

from rest_framwork.response import Response

return  Response (serializer.data)

data가 뭔지 궁금하면 print(serializer.data) 해서 적어보자.

![image-20201005174459194](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005174459194.png)

else: 

​	기능만 구현한다. 글을 쓸수 잇는 form을 주고 실제글을 저장하는 로직을 짜고

rest에선 필요가 없다. 글을 저장하는 로직만 필요!

​		serializer = ArticleListSerializer(data = request.data) 데이타에는 article만드는데 필요한 데이터를 줄 것이다.

​		if serializer.is_valid():

​			serializer.save(raise_exception = True) 통과를 하지못했을 경우 지정가능??

 			return Response(serializer.data)

​		중복코드 정리

![image-20201005174856173](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201005174856173.png)

---

송교수님

댓글

![image-20201006105758509](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006105758509.png)

![image-20201006110250268](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006110250268.png)

![image-20201006110709194](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006110709194.png)

![image-20201006112738690](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006112738690.png)

![image-20201006112741803](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006112741803.png)

댓글아이디로 조회,업데이트,삭제

![image-20201006113345425](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006113345425.png)

알티클에 댓글도 포함시키려면!

![image-20201006114131441](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006114131441.png)

카운터 추가 가능!

![image-20201006114242405](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006114242405.png)

![image-20201006114346328](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006114346328.png)

or 

![image-20201006114522299](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006114522299.png)

![image-20201006114959004](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20201006114959004.png)