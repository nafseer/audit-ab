from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserRoles

# Sign Up Form
class UserRolesForm(UserCreationForm):
    role_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    role_description = forms.CharField(max_length=30, required=False, help_text='Optional')
    module_one = forms.BooleanField()
    module_two = forms.BooleanField()
    module_three = forms.BooleanField()
    module_four = forms.BooleanField()
    module_five = forms.BooleanField()


    class Meta:
        model = UserRoles
        fields = [
            'role_id', 
            'role_name', 
            'role_description', 
            'module_one', 
            'module_two', 
            'module_three', 
            'module_four'
            'module_five'
            ]