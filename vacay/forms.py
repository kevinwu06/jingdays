from django import forms

from .models import UserVacay

class AddForm(forms.ModelForm):

    class Meta:
        model = UserVacay
        fields = ('days_here',)
        widgets = {'days_here': forms.NumberInput(attrs={'step': 1})}