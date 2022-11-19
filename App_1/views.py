# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     # return HttpResponse('Hello, World !!!')
#     return render(request, 'App_1/index.html') # app_name/page.html
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'App_1/index.html'

class AboutPageView(TemplateView):
    template_name = 'App_1/about.html'