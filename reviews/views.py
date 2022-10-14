from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('reviews:index')

    else:
        form = ReviewForm()

    return render(request, 'reviews/create.html', {'form': form})


def index(request):
    users = Review.objects.all().order_by('id')

    return render(request, "reviews/index.html", {'users': users})


def detail(request, review_pk):
    review = Review.objects.get(id=review_pk)

    return render(request, "reviews/detail.html", {'review': review})


def update(request, review_pk):
    review = Review.objects.get(id=review_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid:
            form.save()

            return redirect("reviews:detail", review_pk)

    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/create.html", {"form": form})


def delete(request, review_pk):
    Review.objects.get(id=review_pk).delete()

    return redirect("reviews:index")