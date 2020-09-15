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
            return redirect('articles:detail')

    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)