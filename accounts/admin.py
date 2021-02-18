from django.contrib import admin
import datetime
from .models import Form
from .models import Profile
# from .models import Register

# Register your models here.
admin.site.register(Form)
admin.site.register(Profile)
# admin.site.register(Register)