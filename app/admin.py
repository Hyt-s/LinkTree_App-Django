import imp
from django.contrib import admin
from .models import LinkTree, Links

admin.site.register(LinkTree)
admin.site.register(Links)