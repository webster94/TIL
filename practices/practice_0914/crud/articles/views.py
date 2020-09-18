from django.shortcuts import render , redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def read(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request,'articles/read.html',context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(data = request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)

    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def update(request,pk):
    article= Article.objects.get(pk=pk) # 불러오는게 먼저다
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article': article,
    }
    return render(request, 'articles/update.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:read')
