from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from App_login.forms import SignUpForm, UserProfileChange

# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    diction = {'form': form, 'registered': registered}
    return render(request, "App_login/signup.html", context=diction)


def sign_in(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
    return render(request, "App_login/login.html", context={'form': form})


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def profile(request):
    return render(request, "App_login/profile.html", context={})


@login_required
def change_profile(request):
    current_user = request.user
    form = UserProfileChange(data=request.POST, instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(data=request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    return render(request, "App_login/change_profile.html", context={'form': form})


@login_required
def change_pass(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, "App_login/change_pass.html", context={'form': form, 'changed': changed})
