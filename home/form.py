from django import forms
class urlsearch(forms.Form):
    url = forms.URLField()

# f = urlsearch()
# print(f.is_valid())