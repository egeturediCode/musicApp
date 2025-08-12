from django import forms
from .models import Playlist, Song

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'songs','image','description']
        labels = {
            'name' :'',
            'songs' :'',
            'image' :'',
            'description':''

        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'create-new-form-name', 
                'placeholder': 'playlist name', 
            }),
            'songs': forms.CheckboxSelectMultiple(attrs={
                'class': 'create-new-form-multiselect',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'create-new-form-image',
            }),
            'description': forms.Textarea(attrs={
                'class': 'create-new-form-description',
                'placeholder': 'add description', 
            }),
        }
