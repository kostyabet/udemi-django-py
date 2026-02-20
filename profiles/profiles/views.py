from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    form_class = ProfileForm
    success_url = '/profiles/'

class ProfilesList(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form,
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#             user = UserProfile(image=request.FILES["image"])
#             user.save()
#             return HttpResponseRedirect('/profiles/')
#
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form,
#         })