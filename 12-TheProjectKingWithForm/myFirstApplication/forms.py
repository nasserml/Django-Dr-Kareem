from django import forms


class Wow(forms.Form):
    
    x = forms.CharField(label = 'Enter your prefered message: '
                        , initial='my Message',
                        min_length=5)