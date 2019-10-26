from django import forms
from .models import RegisterComedian

class RegisterComedianForm(forms.ModelForm):
    class Meta:
        model = RegisterComedian
        fields = ('firstname', 'lastname', 'about', 'email', 'phoneno',
                  'profile_pic', 'videos', 'fb_link', 'insta_link',
                  'twitter_link', 'youtube_link')
