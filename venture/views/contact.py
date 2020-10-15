from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from venture.models.contact import Contact


# Create your views here.


class ContactUs(View):

    def get(self, request):
        return render(request, 'contact.html', {})

    def post(self, request):
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        number = request.POST['number']
        text = request.POST['text']

        send_mail(
                  number,
                  text,
                  email,
                  ['sivaramkrishna320@gmail.com'],

                  )

        context = {
            'name': name,
            'subject': subject,
            'email': email,
            'number': number,
            'text': text,

        }
        return render(request, 'contact.html', context)






