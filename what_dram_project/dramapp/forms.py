from django import forms


class Comments(forms.Form):
	username = forms.CharField(max_length=30)
	whisky = forms.CharField(max_length=30)
	comments = forms.CharField(initial="Replace with comment", max_length=400)
