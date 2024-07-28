
#rom django.shortcuts import renderfrom
from django.views.generic import TemplateView
from .models import Publication, Newsletter
from django.http import HttpResponse
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def  get_context_data(self, **kwargs):
      context = {
        'publication_list': Publication.objects.all()
    }
      return context

class AboutView(TemplateView):
    template_name = 'about.html'


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'

    def  get_context_data(self, **kwargs):
     blog_pk = kwargs['pk']

     context = {
        'publication_list': Publication.objects.get(id=blog_pk)
    }
     return context

def newsletter_email_view(request):
    print('это ваш данные от ПОСТ запроса', request.POST)

    input_email = request.POST['email']


    Newsletter.objects.create(email=input_email)
    return HttpResponse("<h1>Ваше сообщение было создано!</h1>")