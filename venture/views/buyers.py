from django.views import View
from django.shortcuts import render
from venture.models.buyers import Buyer
from venture.models.video import Video


class Buyers(View):
    def get(self, request):
       reviews = Buyer.objects.all()
       rev = reversed(reviews)
       files = Video.objects.all()
       template = 'buyers.html'
       context = {
           'rev': rev,
           'files': files
       }
       return render(request, template, context)

