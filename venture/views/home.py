from django.shortcuts import render
from venture.models import Property
from django.views import View
from venture.models import Detail

# Create your views here.


class Venture(View):
    def get(self, request):
        prop = Property.objects.all()
        property_list = reversed(prop)
        template = 'home.html'
        context = {
            'property_list': property_list
        }

        return render(request, template, context)


class PropertyDetail(View):
    def get(self, request, id):
       details = Detail.objects.get(id=id)

       template = 'detail.html'
       context = {
          'details': details
        }

       return render(request, template, context)
