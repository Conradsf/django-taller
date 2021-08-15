from django import forms

class contact_form(forms.Form):

  subject=forms.CharField()
  email=forms.EmailField()
  message=forms.CharField()