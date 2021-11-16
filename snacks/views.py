from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from snacks.models import Snack
# Create your views here.

class SnackListView(ListView):
    template_name = "snacks_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snacks_details.html"
    model = Snack
    context_object_name = "snack_object"
