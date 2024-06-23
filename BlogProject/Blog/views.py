from django.shortcuts import render,redirect
from Blog.models import Post,Comments
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
msg = []
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts': posts,})

@login_required()
def make_post(request):
    if request.method == "POST":
        post_data = request.POST
        new_post = Post(title=post_data['title'],body=post_data['body'],user=request.user)
        new_post.save()
        return redirect('home')
def create_post(request):
    if request.user.is_authenticated:
        return render(request,'post.html')
    else:
        messages.error(request,"User Must Login to Create Post")
        return redirect('home')
def user_login(request):
    msg = []
    if request.method == 'POST':
        email = request.POST.get('user_email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            msg.append(user)
            return render(request, 'login.html', {'error_msg':msg})
    return render(request, 'login.html',{'error_msg':msg})

def user_signup(request):

    if request.method == 'POST':
        email = request.POST.get('user_email')
        name = request.POST.get('user_name')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email=email,username=name,password=password)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'signup.html',{'error_msg': "User alreday register Please click below link to Login"} )

    return render(request, 'signup.html',)

@login_required
def user_logout(request):
    logout(request)
    messages.error(request,'User logged out')
    return redirect('home')
