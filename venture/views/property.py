from django.shortcuts import render

from django.views import View
from venture.models import Property


class PropertyList(View):
    def get(self, request):
      property_list = Property.objects.all()
      template = 'list.html'
      context = {
        'property_list': property_list
      }

      return render(request, template, context)


