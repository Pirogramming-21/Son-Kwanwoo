from django.shortcuts import render, redirect
from .models import Reviews

def review_list(request):
    reviews = Reviews.objects.all()
    
    for review in reviews:
        review.running_time_hours = review.running_time // 60
        review.running_time_minutes = review.running_time % 60
    
    context = {
        "reviews": reviews
    }
    return render(request, 'review_list.html', context)

def review_create(request):
    genre_choices = Reviews.genre_choices
    if request.method=="POST":
        Reviews.objects.create(
            title=request.POST["title"],
            year=request.POST["year"],
            genre=request.POST["genre"],
            rank=request.POST["rank"],
            director=request.POST["director"],
            actor=request.POST["actor"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
        )
        return redirect("/reviews/")
    return render(request, "review_create.html", {"genre_choices": genre_choices})

def review_detail(request, pk):
    review = Reviews.objects.get(id=pk)
    
    review.running_time_hours = review.running_time // 60
    review.running_time_minutes = review.running_time % 60
    
    try:
        previous_id = Reviews.objects.filter(id__lt=pk).order_by("-id")[0].pk
    except IndexError:
        previous_id = None
    
    try:
        next_id = Reviews.objects.filter(id__gt=pk).order_by("id")[0].pk
    except IndexError:
        next_id = None
    
    context={
        "review":review,
        "previous_post_id":previous_id,
        "next_post_id":next_id,
    }
    return render(request,'review_detail.html', context)

def review_update(request, pk):
    genre_choices = Reviews.genre_choices
    review=Reviews.objects.get(id=pk)
    if request.method=="POST":
        review.title=request.POST["title"]
        review.year=request.POST["year"]
        review.genre=request.POST["genre"]
        review.rank=request.POST["rank"]
        review.director=request.POST["director"]
        review.actor=request.POST["actor"]
        review.running_time=request.POST["running_time"]
        review.content=request.POST["content"]
        
        review.save()
        return redirect(f"/reviews/{pk}")
    
    context={
        "review":review,
        "genre_choices": genre_choices
    }
    return render(request, 'review_update.html', context)

def review_delete(request,pk):
    if request.method=="POST":
        review=Reviews.objects.get(id=pk)
        review.delete()
        return redirect("/reviews/")
    
    return redirect("/reviews/")