from django.urls import path
from .views.home import Venture, PropertyDetail
from .views.property import PropertyList
from .views.contact import ContactUs
from .views.about import AboutUs
from .views.buyers import Buyers

app_name = 'venture'


urlpatterns = [
    path('', Venture.as_view(), name='homepage'),
    path('property/', PropertyList.as_view(), name='property'),
    path('property/<int:id>/', PropertyDetail.as_view(), name='property_detail'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('about/', AboutUs.as_view(), name='about'),
    path('buyers/', Buyers.as_view(), name='buyers'),
]

