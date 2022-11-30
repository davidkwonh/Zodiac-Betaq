from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#   WE HAVE NOW ENTERED FORM CREATION ZONE

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        modal = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user