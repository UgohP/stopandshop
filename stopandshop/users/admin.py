from django.contrib import admin
from .models import *
# Register your models here.

class VendorApplicationAdmin(admin.ModelAdmin):
     list_display = ['user', 'business_name', 'phone_number1']
     model = VendorApplication
admin.site.register(VendorApplication, VendorApplicationAdmin)

class Premium1ApplicationAdmin(admin.ModelAdmin):
     list_display = ['user', 'business_name', 'phone_number1']
     model = VendorApplication
admin.site.register(Premium1Application, Premium1ApplicationAdmin)

class Premium2ApplicationAdmin(admin.ModelAdmin):
     list_display = ['user', 'business_name', 'phone_number1']
     model = VendorApplication
admin.site.register(Premium2Application, Premium2ApplicationAdmin)

class Premium3ApplicationAdmin(admin.ModelAdmin):
     list_display = ['user', 'business_name', 'phone_number1']
     model = Premium3Application
admin.site.register(Premium3Application, Premium3ApplicationAdmin)

class CustomerPremiumApplicationAdmin(admin.ModelAdmin):
     list_display = ['customer', 'first_name', 'phone_number1']
     model = CustomerPremiumAppplication
admin.site.register(CustomerPremiumAppplication, CustomerPremiumApplicationAdmin)

admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(SecurityQuestion)
admin.site.register(VendorVerification)