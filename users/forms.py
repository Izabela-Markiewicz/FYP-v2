from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms import ModelForm
from .models import Review

# Iteration 5
# Register User
# REF: Add Extra Registraion Fields [Youtube] (Codemy.com, 2021)
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    # Add non-standard fields to form
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # Iteration 5
    # Bootstrapify input fields
    # REF: Style Django Registration Forms [Youtube] (Codemy.com, 2021)
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# Iteration 5
# Create User Review
# REF: How To Add Database Forms To A Web Page [Youtube] (Codemy.com, 2021)
class ReviewForm(ModelForm):
    class Meta: 
        model = Review
        fields = ('policeID', 'reviewText', 'feelRating', 'imageYN', 'image')

        widgets = {
            'policeID' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'Police ID'}),
            'reviewText': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Write your review here'}),
            'feelRating' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Area Rating / 5'}),
           # 'imageYN' : forms.TextInput(attrs={'class' : 'form-control'}),
           # 'image' : forms.TextInput(attrs={'class' : 'form-control'}),
        }


"""
REFERENCES:


Iteration 5:
    Codemy.com (2021). Add Extra Registration Fields - Django Wednesdays #25. YouTube. Available at: https://www.youtube.com/watch?v=HdrOcreAXKk [Accessed 20 Feb. 2024].
    Codemy.com (2021). Style Django Registration Forms - Django Wednesdays #26. YouTube. Available at: https://www.youtube.com/watch?v=XapMxdIyLM8 [Accessed 21 Feb. 2024].
    Codemy.com (2021). How To Add Database Forms To A Web Page - Django Wednesdays #7. YouTube. Available at: https://www.youtube.com/watch?v=CVEKe39VFu8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=7 [Accessed 21 Feb. 2024].

‌
‌

"""    