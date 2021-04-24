from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import AddPostForm
from django.views import generic

def BlogPost(request):
    blog = Blog.objects.all()
    form = AddPostForm()
    context={'blogpost':blog}
    return render(request, 'home.html', context)



class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blogg/blogdetail.html'



def AddPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST , request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            writer = request.user
            image = form.cleaned_data['image']
            image = form.cleaned_data['video']
            blog = Blog.objects.create(title = title, content = content, writer = writer, image = image, video = video)
            blog.save()
            return render(request, 'blogg/successfully-add-post.html')

    else:
        form = AddPostForm()
        blog = Blog.objects.all()
    context = {'form':form}
    return render(request, 'blogg/add-article.html', context)




class BlogView(generic.ListView):
    template_name= 'blogg/home.html'
    context_object_name = 'blogpost'

    def get_queryset(self):
        return Blog.objects.all()


def PostLike(request, postid):
    post = Blog.objects.get(id = postid)
    user = request.user
    if user.is_authenticated:
        if user in post.like.all():
            return HttpResponse('!شما این پست را قبلا لایک کردید')
        post.like.add(user)
        return redirect('detail', postid)
    else:
        HttpResponse('یرای لایک کردن لطفا اول وارد سایت شوید')

    

def PostUnlike(request, postid):
    post = Blog.objects.get(id = postid)
    user = request.user
    if user.is_authenticated:
        if user in post.like.all():
            post.like.remove(user)
            return redirect('detail', postid)
        else:
            return HttpResponse('!شما این پست را لایک نکردید')
    else:
        HttpResponse('یرای لایک کردن لطفا اول وارد سایت شوید')