# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404, render


def main(request):
    return render(request, 'base.html')