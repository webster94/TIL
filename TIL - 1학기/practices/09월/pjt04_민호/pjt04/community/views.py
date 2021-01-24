from django.shortcuts import render ,redirect
from .forms import ReviewForm
from .models import Review
from django.views.decorators.http import require_http_methods, require_POST
# Create your views here.

def review_list(request):
    review = Review.objects.order_by('-pk') # 그냥 고정이네! 요고 몰랐다.
    context = {
        'review' :review
    }
    return render(request,'community/review_list.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_detail' ,review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request,'community/form.html',context)


def review_detail(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    context = {
        'review' : review,
    }
    return render(request,'community/review_detail.html',context)
@require_http_methods(['GET','POST'])
def review_update(request,review_pk):
    review = Review.objects.get(pk = review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST,instance = review)
        if form.is_valid():
            form.save()  # 까먹었다..
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm(instance = review)
    context = {
        'form' : form,
        'review' : review
    }
    return render(request,'community/form.html', context)
@require_POST
def review_delete(request,review_pk):
    form = Review.objects.get(pk=review_pk)
    form.delete()
    return redirect('community:review_list')