from django import forms

class Leitor(forms.Form):
    text_area = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols':60, 'rows':12}), label='')
