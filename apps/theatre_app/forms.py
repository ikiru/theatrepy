from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "address",
            "city",
            "state",
            "zip",
            "email",
            "phone",
            "mobile",
            "district",
            "school",
            "gradyear",
            "avatar",
        ]
