from django import forms


class CommentForm(forms.Form):
	username = forms.CharField(label='username', max_length=30)
	whisky = forms.CharField(label='whisky', max_length=30)
	comment = forms.CharField(label='comment', max_length=400)

