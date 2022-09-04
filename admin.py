from django.contrib import admin
from .models import Address, City, District, Ward
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'district','ward', 'street','building', 'house_no')
  
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'name','slug', 'type','namewithtype')
    prepopulated_fields = {"slug": ("name",)} 
   
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'name','slug', 'type','namewithtype','path','pathwithtype','parentcode')
    prepopulated_fields = {"slug": ("name",)} 
   
class WardtAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'name','slug', 'type','namewithtype','path','pathwithtype','parentcode')
    prepopulated_fields = {"slug": ("name",)} 
   
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Ward, WardtAdmin)
admin.site.register(Address, AddressAdmin)