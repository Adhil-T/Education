from django.contrib import admin
from . models import Course, Team, Testimonial, Contact

# Register your models here.
admin.site.register(Course)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Contact)