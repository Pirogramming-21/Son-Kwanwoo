from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post
import json

def post_list(request):
    post, created = Post.objects.get_or_create(id=1, defaults={"like": 0, "comment": ""})
    ctx = {
        'post': post,
    }
    return render(request, 'insta/post_list.html', ctx)

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post = Post.objects.get(id=1)
    post.like += 1
    post.save()
    return JsonResponse({"like": post.like})

@csrf_exempt
def comment_ajax(request):
    req = json.loads(request.body)
    post = Post.objects.get(id=1)
    new_comment = req['comment']
    post.comment += f"\n{new_comment}" if post.comment else new_comment
    post.save()
    return JsonResponse({"comment": post.comment})

@csrf_exempt
def delete_comment_ajax(request):
    req = json.loads(request.body)
    post = Post.objects.get(id=1)
    comment_to_delete = req['comment']
    comments = post.comment.split('\n')
    comments = [c for c in comments if c != comment_to_delete]
    post.comment = '\n'.join(comments)
    post.save()
    return JsonResponse({"comment": post.comment})