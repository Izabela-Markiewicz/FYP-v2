from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms import ModelForm
from .models import Review
from areas.models import PoliceDivision

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
    # Change PoliceID input to policeName dropdown
    # REF: ChatGPT (2024): 'In the review form, instead of asking for policeID, i want it to ask for policeName from a dropdown, and depending on dopdown selected save it back as policeID in database. i dont want the user seeing the policeID. This is the current code for my models, from, and views.'
    policeName = forms.ModelChoiceField(queryset=PoliceDivision.objects.all(), empty_label=None, 
                                         widget=forms.Select(attrs={'class': 'form-control'}), 
                                         label='Select Area')

    class Meta: 
        model = Review
        fields = ('policeName', 'reviewText', 'feelRating', 'image')

    	# REF: Change Labels in Django Form (Django Software Foundation, 2022)
        labels = {
            'reviewText': 'Review',
            'feelRating': 'Safety Rating (1-5)',
            'image': 'Upload Image (Optional)',
        }

        widgets = {
            'reviewText': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Write your review here'}),
            'feelRating' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Area Rating / 5'}),
        }

    # REF: ChatGPT (2024): 'In the review form, instead of asking for policeID, i want it to ask for policeName from a dropdown, and depending on dopdown selected save it back as policeID in database. i dont want the user seeing the policeID. This is the current code for my models, from, and views.'
    def save(self, commit=True):
        review = super().save(commit=False)
        police_name = self.cleaned_data['policeName']
        police_division = PoliceDivision.objects.get(policeName=police_name)
        review.policeID = police_division
        if commit:
            review.save()
        return review  


"""
REFERENCES:


Iteration 5:
    Codemy.com (2021). Add Extra Registration Fields - Django Wednesdays #25. YouTube. Available at: https://www.youtube.com/watch?v=HdrOcreAXKk [Accessed 20 Feb. 2024].
    Codemy.com (2021). Style Django Registration Forms - Django Wednesdays #26. YouTube. Available at: https://www.youtube.com/watch?v=XapMxdIyLM8 [Accessed 21 Feb. 2024].
    Codemy.com (2021). How To Add Database Forms To A Web Page - Django Wednesdays #7. YouTube. Available at: https://www.youtube.com/watch?v=CVEKe39VFu8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=7 [Accessed 21 Feb. 2024].
    ChatGPT (2024). 'In the review form, instead of asking for policeID, i want it to ask for policeName from a dropdown, and depending on dopdown selected save it back as policeID in database. i dont want the user seeing the policeID. This is the current code for my models, from, and views.'
    Django Software Foundation (2022). change label of a field in a form. [online] Django Forum. Available at: https://forum.djangoproject.com/t/change-label-of-a-field-in-a-form/14227 [Accessed 23 Feb. 2024].

‌
‌
‌

"""    