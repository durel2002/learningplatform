from django import forms

# Login form

class SigninForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'barista@roastandray.com'}))
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))



class SignupForm(forms.Form):
    countries =[
    ('', '--Select a Country--'),
    ('CM','Cameroon'),
    ('NG', 'Nigeria'),
    ('CA','Canada'),    
     ]
    firstName = forms.CharField(label="Enter your first name", widget=forms.TextInput(attrs={'placeholder':'joe'}))
    lastName = forms.CharField(label="Enter your first name", widget=forms.TextInput(attrs={'placeholder':'doe'}))
    phoneNumber = forms.CharField(label="Enter your password", widget=forms.TextInput(attrs={'placeholder':'Enter your password'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'barista@roastandray.com'}))
    country = forms.ChoiceField(choices=countries, widget=forms.Select(attrs={'class': 'form-control'}) )
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    confirmPassword = forms.CharField(label="Enter your password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))