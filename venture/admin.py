from django.contrib import admin
from .models.property import Property
from .models.slider import Slider
from .models.buyers import Buyer
from .models.video import Video
from .models.detail import Detail
from .models.contact import Contact

# Register your models here


class AdminProperty(admin.ModelAdmin):
    list_display = ['name', 'location']


class AdminDetail(admin.ModelAdmin):
    list_display = ['name', 'address']


admin.site.register(Property, AdminProperty)
admin.site.register(Slider)
admin.site.register(Buyer)
admin.site.register(Video)
admin.site.register(Detail, AdminDetail)
admin.site.register(Contact)






