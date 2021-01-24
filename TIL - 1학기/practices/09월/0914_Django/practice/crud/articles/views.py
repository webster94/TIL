from django.shortcuts import render,redirect
from.models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    return render(request, "articles/index.html", context )

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article()
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:index')
    else:
        return render(request,'articles/create.html')