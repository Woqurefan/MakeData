from django.contrib import admin

# Register your models here.
import inspect,sys
from Myapp.models import *

cls_members = inspect.getmembers(sys.modules[__name__],inspect.isclass)
for name,cls in cls_members:
    admin.site.register(cls)