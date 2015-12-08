from django import forms

from .models import UserVacay

class AddForm(forms.ModelForm):

    class Meta:
        model = UserVacay
        fields = ('days_away', 'days_here',)