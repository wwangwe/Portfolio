from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Project


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wangwe:home')
    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'projects': Project.objects.all().order_by('date')
    }

    return render(request, 'wangwe/index.html', context)
    