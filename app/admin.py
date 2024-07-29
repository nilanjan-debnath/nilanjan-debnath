from django.contrib import admin
from .models import Projects, Expriences, Hackathons, Certifications

# Register your models here.
admin.site.register(Projects)
admin.site.register(Expriences)
admin.site.register(Hackathons)
admin.site.register(Certifications)