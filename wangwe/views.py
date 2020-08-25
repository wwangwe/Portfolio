from django.shortcuts import render, redirect
from .forms import FeedbackForm


def index(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('wangwe:home')
	else:
		form = FeedbackForm()

	return render(request, 'wangwe/index.html', {'form': form})


# name = form.cleaned_data['name']
# 			email = form.cleaned_data['email']
# 			message = form.cleaned_data['message']