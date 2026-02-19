from django import forms

from reviews.models import Review


# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=100)
#     review_text = forms.CharField(label="Your Review Text", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'