from django import forms
from .models import Feedback, Project


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})
        self.fields['email'].widget.attrs.update({'placeholder': "What's your email?"})
        self.fields['message'].widget.attrs.update({'rows': 3})
