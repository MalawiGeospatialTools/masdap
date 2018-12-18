from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)

	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		name = cleaned_data.get('name')
		email = cleaned_data.get('email')
		message = cleaned_data.get('message')
		if not name and not email and not message:
			raise forms.ValidationError('You have to write somenthing!')
