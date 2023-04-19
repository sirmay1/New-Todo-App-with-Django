# Build A Cool To-Do App With Django and Python! tutorial Codemy.com on YouTube.com
# forms.py doesn't exist when creating your app. Similarily to the urls.py file you have to create this as well.
# (12:30)

from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]