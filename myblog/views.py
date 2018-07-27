from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

'''
    elif choice == "선택 2":
        return JsonResponse({"user_key": "user", "type": "text", "content": "학식메뉴"})
    elif choice == "선택 3":
        return JsonResponse({"user_key": "user", "type": "text", "content": ""})
    keyboard()
'''

@csrf_exempt
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    user = received_json_data['user_key']
    choice = received_json_data['content']
    if choice == "선택 1":
        return JsonResponse({'message': {'text': '텍스트 출력 ~~~'},'keyboard': {'type': 'buttons','buttons': ["선택 1", "선택 2", "선택 3"]}})


def keyboard(request):
    return JsonResponse({"type": "buttons",  "buttons" : ["선택 1", "선택 2", "선택 3"]})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/post_edit.html', {'form': form})