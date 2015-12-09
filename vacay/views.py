from django.shortcuts import render, get_object_or_404, redirect
from .models import UserVacay
from .forms import AddForm

def home(request):
    user_vacay = UserVacay.objects.all()
    return render(request, 'vacay/home.html', {'user_vacay': user_vacay})
    
def add(request):
    post = get_object_or_404(UserVacay)
    if request.method == "POST":
        form = AddForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.vacay_days = post.days_here/5
            post.save()
            return redirect('home')
    else:
        form = AddForm(instance=post)
    return render(request, 'vacay/add.html', {'form': form})
