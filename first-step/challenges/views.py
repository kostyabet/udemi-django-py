from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

months = {
    "january": "Go to the gim",
    "february": "Go to the gim",
    "march": "Go to the gim",
    "april": "Go to the gim",
    "may": "Go to the gim",
    "june": "Go to the gim",
    "july": "Go to the gim",
    "august": "Go to the gim",
    "september": "Go to the gim",
    "october": "Go to the gim",
    "november": "Go to the gim",
    "december": "Go to the gim",
}

def month_int(response, month):
    l = list(months.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Month is out of range</h1>')

    redirect_month = l[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def month(request, month):
    try:
        selected_month_info = months[month]
        return render(request, 'challenges/challenges.html', {
            "title": f"{selected_month_info.capitalize()} challenge",
            "header": f"{selected_month_info.capitalize()} challenge is...",
            "text": selected_month_info,
        })
    except:
        raise Http404()

def index(request):
    l = list(months.keys())

    return render(request, 'challenges/index.html', {
        "months": l
    })