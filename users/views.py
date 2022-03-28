from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def users(request):
    users = User.objects
    return render(request, 'users/users.html', {'users':users})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = request.user
            user.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'users/registration.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = request.user
            user.save()
            return redirect('users')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_edit.html', {'form': form})