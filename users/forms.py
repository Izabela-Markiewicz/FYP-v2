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
    # Iteration 6
    # Only allow increments of 0.5 for feelRating
    # REF: (Copilot, 2024) - 'How do I allow only increments of 0.5?'
    RATING_CHOICES = [(None, '-----')] + [(i/2, str(i/2)) for i in range(2, 11)]

    # Change PoliceID input to policeName dropdown
    policeName = forms.ModelChoiceField(queryset=PoliceDivision.objects.all(), empty_label=None, 
                                         widget=forms.Select(attrs={'class': 'form-control'}), 
                                         label='Select Area')
    # Use a ChoiceField for feelRating
    feelRating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), required=True, label='Safety Rating: 1 (Unsafe) - 5 (Safest)')
    
    # Add checkbox for 'anon' field
    anon = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False, initial=False, label='Anonymous')

    class Meta: 
        model = Review
        fields = ('policeName', 'feelRating', 'reviewText', 'image', 'anon')

        labels = {
            'reviewText': 'Comment (Optional)',
            'feelRating': 'Safety Rating (1-5)',
            'image': 'Upload Image (Optional)',
        }

        widgets = {
            'reviewText': forms.Textarea(attrs={'class' : 'form-control', 'placeholder':'Write your review here', 'rows': 4}),
            'feelRating': forms.Select(attrs={'class': 'form-control dropdown-toggle', 'data-toggle': 'dropdown'}),
        }

    def save(self, commit=True):
        review = super().save(commit=False)
        police_name = self.cleaned_data['policeName']
        police_division = PoliceDivision.objects.get(policeName=police_name)
        review.policeID = police_division
        if commit:
            review.save()
        return review      
