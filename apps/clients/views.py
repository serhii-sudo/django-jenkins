from django.shortcuts import render
from django.views import View

from apps.clients.models import Client


class Home(View):
    template_name = 'clients/data.html'

    def get(self, request):
        clients = Client.objects.all()
        return render(request, self.template_name, {'clients': clients})
