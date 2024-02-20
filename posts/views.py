from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index (request):
   # If the method is POST
    if request.method == 'POST':
       form = PostForm(request.POST, request.FILES)
       #if the form is valid
       if form.is_valid():
           #yes, save
           form.save()
           #redirect to home
           return HttpResponseRedirect('/')

       else:
           #no, show error
           return HttpResponseRedirect(form.errors.as_json())

    #get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    #show
    return render(request,'posts.html',
                  {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/") 


def likes(request, post_id):
    post= Post.objects.get(id=post_id)
    post.like += 1    # post.like = post.like + 1
    post.save()
    return HttpResponseRedirect('/')#keeps you in homepage

def edit (request, post_id):
   # If the method is POST
    if request.method == 'GET':
       posts= Post.objects.get(id=post_id)
       return render(request, 'edit.html',{'posts':posts})

    if request.method == "POST":
       editposts = Post.objects.get(id = post_id)
       form = PostForm(request.POST, request.FILES, instance=editposts)
       #if the form is valid
       if form.is_valid():
           #yes, save
           form.save()
           #redirect to home
           return HttpResponseRedirect('/')

       else:
           #no, show error
           return HttpResponse("not valid")

    