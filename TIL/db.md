1. article 모델 작성

```
class Comment(models.Model):
    content = models.CharField(max_length = 150) #  최대길이
    article = models.ForeignKey(Article,on_delete=models.CASCADE)# 필수인자 2개! 1. 바라볼곳 2. 참조하는 녀석의 코멘트를 어떻게할것인가? Cascade 바라보는 곳이 삭제되면 같이 사라지겠다.
    
```

2. url 작성

```

    path('<int:article_pk>/comments/',views.comment_create,name = 'comment_create'),
```

3. vieiw작성

```

```

4. form 작성 근데 view 작성 전에 필요

```
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
```

5. detail.html에 작성

   ```
   <form action="{% url 'articles:comment_create' article.pk %}" method="post">
           {% csrf_token %}
           {{ comment_form.as_p }}
           <button>댓글쓰기</button>
       </form>
       {% for comment in comments %}
           <h4>{{ comment.content }}</h4>
       {% endfor %}
   ```

   ![image-20200922101043410](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922101043410.png)

   



딜리트

![image-20200922102114827](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922102114827.png)

딜리트디테일

![image-20200922102207730](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922102207730.png)

인자 2개!

![image-20200922102224405](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922102224405.png)



---



## 송빈산 쌤 데이터베이스에 대한강의



![image-20200922103119738](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922103119738.png)

![image-20200922103332650](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922103332650.png)

![image-20200922103357769](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922103357769.png)

code ~/.bashrc

winpty sqlite3

![image-20200922113419715](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922113419715.png)

![image-20200922113653049](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922113653049.png)

sqlite turotial.sqlite3



.mode csv

.import users.csv users

users에서 age가 30 이상인 사람만 가져온다면?

sqlite>SELECT * FROM users WHERE age>=30;









SELECT * FROM users;



![image-20200922133133147](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922133133147.png)

![image-20200922133252675](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922133252675.png)

평균나이구하는 법(조건은 웨어!)

sqlite> SELECT AVG(AGE) FROM users WHERE age >= 30;  
35.1763285024155



![image-20200922133822134](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922133822134.png)

![image-20200922134018785](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134018785.png)

![image-20200922134055761](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134055761.png)

![image-20200922134213701](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134213701.png)

![image-20200922134453872](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134453872.png)

![image-20200922134503024](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134503024.png)

![image-20200922134535654](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134535654.png)

![image-20200922134715803](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134715803.png)

![image-20200922134755634](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134755634.png)

![image-20200922134840143](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922134840143.png)

![image-20200922140325457](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922140325457.png)

> group by





practice

![image-20200922160605967](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922160605967.png)

![image-20200922161134852](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922161134852.png)

> sql 에 정보입력되면 바로나오게끔함

![image-20200922161213797](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922161213797.png)

![image-20200922174240564](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200922174240564.png)

> 계좌가 가장 많은 첫번째 사람 뽑아내는법