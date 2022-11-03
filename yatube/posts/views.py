from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main yatube page')


def group_posts(request, gk):
    return HttpResponse(f'This is funny test page number {gk} :)')
