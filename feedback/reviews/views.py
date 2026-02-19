from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = '/thank-you'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# Also has Delete/Update
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/reviews'

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank You'
        return context

class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query_set = super().get_queryset()
        data = base_query_set.filter(rating__gt=3)
        return data

class ReviewsDetailView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review