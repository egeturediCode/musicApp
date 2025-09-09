from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="",
        widget = forms.TextInput(attrs={
            'class': 'form-username',
            'placeholder': 'Username'
    }))
    
    password = forms.CharField(label="",
        widget=forms.PasswordInput(attrs={
            'class' : 'form-password',
            'placeholder' : 'Password',
    }))


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={
        'class' : 'form-firstname',
        'placeholder' : 'First Name'
    }))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={
        'class' : 'form-lastname',
        'placeholder' : 'Last Name'
    }))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={
        'class' : 'form-username',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={
        'class' : 'form-password',
        'placeholder' : 'Password'
    }))
    confirm = forms.CharField(label="",widget=forms.PasswordInput(attrs={
        'class' : 'form-confirm',
        'placeholder' : 'Confirm Password'
    }))

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler eşleşmedi.")
        
        values = {
            "username" : username,
            "password" : password,
            "first_name" : first_name,
            "last_name" : last_name
        }

        return values