from .models import Article
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
# article을 다 가져와서 목록을 보여줄게요
# 데이터베이스에서 가져와보자
    articles = Article.objects.all()[::-1]  # python이 정렬
    articles = Article.objects.order_by('-pk') # db에서 정렬
    # -pk는 내림차순을 정렬이된다.  원본변경의 차이

    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html',context)


def new(request):
    return render(request, 'articles/new.html') 
    # 보여주기만 하면 된다.

def create(request):
    title = request.POST.get('title')  # new에서 보낸 정보
    content = request.POST.get('content') # new에서 보낸 정보
    # 받은 정보를 db에 저장
    # article 테이블에 정보저장
    article= Article()
    article.title = title
    article.content = content
    article.save()
    # 2
    # Article.objects.create(title=title, content= content)
    # 3
    # article = Article(title = title )
    # article/.save()
    # 글 잘 써졌습니다 ~ 하고 알려줌
    # 글이 다 써졌으면, 해당 글 디테일 페이지로 redirecting

    return redirect('articles:detail',article.pk)


def detail(request, article_pk):
    # article_pk에 해당하는 article을 찾아서 보여준다.
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }

    return render(request,'articles/detail.html', context)

def delete(request,article_pk):
     # article_pk에 해당하는 article을 찾아서 삭제한다.
     article = Article.objects.get(pk=article_pk)
     article.delete()
     # 삭제완료
     return redirect('articles:index')

    
def update(request, article_pk):
    # 수정할수 있는 화면을 보여주세요
    # article_pk 로 정보 가져와서 넘겨주면 되겠네!
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/update.html', context)


def modify(request, article_pk):
    #1. 수정대상 찾기.
    article = Article.objects.get(pk=article_pk)
    #2. 수정할 데이터 가져오기.
    title = request.POST.get('title')# update에서 보내준 데이터
    content = request.POST.get('content') # update에서 보내준 데이터
    #3. 수정 대상을 수정할 데이터로 수정하기.
    article.title = title
    article.content = content
    article.save()
    #4. detail 페이지 redirection
    return redirect('articles:detail', article.pk)