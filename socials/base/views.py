from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from itertools import chain
import random

from django.contrib.auth import get_user_model
from .models import Profile, Post, Comment, LikePost, FollowersCount
from .forms import (
    PostForm, ProfilePageForm, EditProfileNewForm,
    CommentForm, EditForm, PasswordChangingForm
)

User = get_user_model()


# =========================
# HOME
# =========================
@login_required(login_url='signup')
def home(request):
    user_object = request.user
    user_profile, _ = Profile.objects.get_or_create(user=user_object)

    all_users = User.objects.all()
    all_posts = Post.objects.all().order_by('-id')
    all_profiles = Profile.objects.all()
    count_posts = all_posts.count()

    my_user = [user_profile]
    suggestion_users = [u for u in all_profiles if u not in my_user]
    random.shuffle(suggestion_users)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'all_users': all_users,
        'all_posts': all_posts,
        'all_profile': all_profiles,
        'count_posts': count_posts,
        'suggestion_users': suggestion_users,
    }
    return render(request, "base/home.html", context)


# =========================
# PROFILE VIEW
# =========================
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'base/Otherprofile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        logged_in_user_posts = Post.objects.filter(author=page_user)

        if FollowersCount.objects.filter(user=page_user.user.username).exists():
            button_text = 'UnFollow'
        else:
            button_text = 'Follow'

        user_followers = FollowersCount.objects.filter(user=page_user.user.username).count()
        user_following = FollowersCount.objects.filter(follower=page_user.user.username).count()

        context.update({
            "page_user": page_user,
            "logged_in_user_posts": logged_in_user_posts,
            "num_posts": logged_in_user_posts.count(),
            "button_text": button_text,
            "user_followers": user_followers,
            "user_following": user_following,
        })
        return context


# =========================
# AUTH
# =========================
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        login_username = request.POST.get('username')
        user_password = request.POST.get("password")
        user = authenticate(request, username=login_username, password=user_password)

        if user:
            auth_login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "base/login.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST['email'].strip()
        password = request.POST['password']
        username = request.POST['username']

        if not email or not password or not username:
            messages.error(request, "Please fill all fields.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            user = User.objects.create(
                email=email,
                username=username,
                password=make_password(password)
            )
            auth_login(request, user)
            return redirect('/create_profile_page')

    return render(request, "base/signup.html")


def logout(request):
    auth_logout(request)
    return redirect('/')


# =========================
# FRIENDS
# =========================
class FriendView(ListView):
    model = Profile
    template_name = 'base/friends.html'
    ordering = ['-id']


# =========================
# POSTS
# =========================
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'base/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'base/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'base/delete_post.html'
    success_url = reverse_lazy('home')


# =========================
# PROFILE CRUD
# =========================
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "base/create_user_profile.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    form_class = EditProfileNewForm
    template_name = 'base/edit_profile_page.html'
    success_url = reverse_lazy('home')


# =========================
# PASSWORD CHANGE
# =========================
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'base/password_success.html')


# =========================
# COMMENTS
# =========================
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'base/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


# =========================
# LIKE SYSTEM (SAFE)
# =========================
@login_required(login_url='signup')
def like_post(request):
    post_id = request.GET.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    username = request.user.username

    like = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like:
        like.delete()
        post.no_of_likes = max(0, post.no_of_likes - 1)
    else:
        LikePost.objects.create(post_id=post_id, username=username)
        post.no_of_likes += 1

    post.save(update_fields=["no_of_likes"])
    return redirect('home')


# =========================
# SEARCH
# =========================
@login_required(login_url='signup')
def search(request):
    user_profile = get_object_or_404(Profile, user=request.user)

    username_profile_list = []
    if request.method == 'POST':
        username = request.POST['username']
        username_profile_list = Profile.objects.filter(username__icontains=username)

    return render(
        request,
        'base/search.html',
        {
            'user_profile': user_profile,
            'username_profile_list': username_profile_list,
        }
    )


# =========================
# FOLLOW
# =========================
@login_required(login_url='signup')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        obj = FollowersCount.objects.filter(follower=follower, user=user).first()
        if obj:
            obj.delete()
        else:
            FollowersCount.objects.create(follower=follower, user=user)

    return redirect('home')
