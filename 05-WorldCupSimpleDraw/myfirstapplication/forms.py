from django import forms

class InputForm(forms.Form):
    x = forms.IntegerField(label="Enter first Number:")
    y = forms.IntegerField(label="Enter second Number:")
    

class PrimeForm(forms.Form):
    x = forms.IntegerField(label="Enter a Number:")



class WorldcupForm(forms.Form):
    countries = forms.CharField(widget=forms.Textarea,label="Enter Countries sepaated by - ")


