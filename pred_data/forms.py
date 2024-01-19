from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'

    age = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'})
    )

    gender = forms.ChoiceField(
        choices=[(1, 'Male'), (0, 'Female')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )


    chest_pain = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Chest Pain'})
    )

    resting_bp = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Resting Blood Pressure'})
    )

    cholesterol = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cholesterol'})
    )

    fasting_blood_suger = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fasting Blood Sugar'})
    )

    resting_ecg = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Resting ECG'})
    )

    max_heart_rate = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Max Heart Rate'})
    )

    exercise_angina = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Exercise Angina'})
    )

    oldpeak = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Oldpeak'})
    )

    ST_slope = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ST Slope'})
    )
