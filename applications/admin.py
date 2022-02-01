from encodings import search_function
from django.contrib import admin
from .models import Applications

# Register your models here.

class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email', 'birth', 'phone', 'education', 'desired_job', 'desired_start', 'desired_end', 'languages', 'volunteer_experience', 'recommendations', 'skills', 'volunteer_book', 'why', 'video', 'comments' )
    list_filter = ('id', 'fio', 'education', 'desired_job', 'desired_start', 'desired_end', 'languages')
    search_fields = ('id', 'fio', 'email', 'birth', 'phone', 'education', 'desired_job', 'desired_start', 'desired_end', 'languages', 'volunteer_experience', 'recommendations', 'skills', 'volunteer_book', 'why', 'video', 'comments')


admin.site.register(Applications, ApplicationsAdmin)