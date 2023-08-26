from django.contrib import admin
from GGDC.models import *

# Register your models here.



class FacultyAdmin(admin.ModelAdmin):
    list_display = ('Picture_tag','name','qualification','Experience','department','designation','status')
    search_fields = ('name',)
    list_filter = ('department','status')
    list_per_page = 10

class PrincipalAdmin(admin.ModelAdmin):
    list_display = ('Picture_tag','name','duration','joining_date', 'leaving_date')
    search_fields = ('name',)
    list_per_page = 10

class BooksUpload(admin.ModelAdmin):
    list_display = ('title','department')
    search_fields = ('title',)
    list_filter = ('department',)
    list_per_page = 10

class NewsAdmin(admin.ModelAdmin):
    list_display =('title','date_uploaded')
    list_per_page = 10

class NewsBannerAdmin(admin.ModelAdmin):
    list_display = ('Picture_tag','title','date_uploaded')
    search_fields = ('title',)
    list_per_page = 10

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('Picture_tag','title','date')
    search_fields = ('title',)
    list_per_page = 10

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('Picture_tag','date')
    # search_fields = ('title',)
    list_per_page = 10


admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Principal,PrincipalAdmin)
admin.site.register(Books,BooksUpload)
admin.site.register(News,NewsAdmin)
admin.site.register(NewsBanner, NewsBannerAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Firstyearform)


