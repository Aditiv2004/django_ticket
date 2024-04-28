from django.contrib import admin


from django.contrib.auth.models import Permission




admin.site.site_header = 'Ticketing System'





from .models import Ticket 
from asgiref.sync import async_to_sync, sync_to_async


admin.site.register(Permission)
class TicketAdmin(admin.ModelAdmin):
    #list_filter = ["status","priority"]
    def save_model(self, request, obj, form, change):    
        if request.user.user_permissions.filter(codename="add_ticket").exists():    
            obj.user = request.user
        super().save_model(request, obj, form, change)

     
    def get_queryset(self, request):
        if request.user.is_superuser: 
            return Ticket.objects.all()
        if request.user.user_permissions.filter(codename="add_ticket").exists(): 
            return Ticket.objects.filter(user=request.user)
        else:
            return Ticket.objects.filter(technician=request.user).order_by("-priority")
    
    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ["title","description","rating","document_upload","priority",'solution','status','user','technician',"complaint_type"]
        if request.user.user_permissions.filter(codename="add_ticket").exists(): 
            return ["title","document_upload","rating","description","priority"]
        if obj.status!="created": 
            return ["title","description",'solution',"rating","document_upload",'status']
 
         
  
    
    list_display = ("title", "description", "created_date", "resolve_date")  
 
       






admin.site.register(Ticket, TicketAdmin)
 