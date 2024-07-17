from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from .forms import PostForm

# 게시물 목록 보기
def main(req):
    posts = Posts.objects.all()
    search_txt = req.GET.get("search_txt")
    
    if search_txt:
        posts = posts.filter(title__icontains=search_txt)
        
    context = {
        "posts": posts
    }
    return render(req, 'posts/post_list.html', context)

# 게시물 생성
def post_create(req):
    if req.method == "GET":
        form = PostForm()
        context = {'form': form}
        return render(req, 'posts/post_create.html', context)

    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
        post = form.save()
        return redirect('posts:detail', pk=post.pk)  # 네임스페이스와 URL 패턴 이름 확인

    context = {'form': form}
    return render(req, 'posts/post_create.html', context)

# 게시물 상세 보기
def post_detail(req, pk):
    post = get_object_or_404(Posts, pk=pk)
    related_posts = Posts.objects.filter(tool=post.tool).exclude(pk=pk)
    
    context = {
        "post": post,
        "related_posts": related_posts
    }
    return render(req, 'posts/post_detail.html', context)

# 게시물 업데이트
def post_update(req, pk):
    post = get_object_or_404(Posts, pk=pk)
    if req.method == "GET":
        form = PostForm(instance=post)
        context = {'form': form, 'post': post}  # 'post'를 추가하여 템플릿에서 사용할 수 있게 함
        return render(req, 'posts/post_update.html', context)

    form = PostForm(req.POST, req.FILES, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:detail', pk=post.pk)  # 네임스페이스와 URL 패턴 이름 확인

    context = {'form': form, 'post': post}
    return render(req, 'posts/post_update.html', context)

# 게시물 삭제
def post_delete(req, pk):
    post = get_object_or_404(Posts, pk=pk)
    if req.method == "POST":
        post.delete()
        return redirect('posts:main')
    context = {
        "post": post
    }
    return render(req, 'posts/post_confirm_delete.html', context)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_interest(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')
        post = get_object_or_404(Posts, id=post_id)

        try:
            post.interest = int(post.interest)
        except ValueError:
            return JsonResponse({'error': 'Invalid interest value'}, status=400)

        if action == 'up':
            post.interest += 1
        elif action == 'down':
            post.interest -= 1

        post.save()

        return JsonResponse({'interest': post.interest})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def update_idea_star(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Posts, id=post_id)

        post.idea_star = not post.idea_star
        post.save()

        return JsonResponse({'idea_star': post.idea_star})

    return JsonResponse({'error': 'Invalid request'}, status=400)