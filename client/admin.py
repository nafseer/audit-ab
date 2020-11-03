from django.contrib import admin
from .models import ClientsProfile,DesignationMasterNew,RolesMasterNew,ClientsTeam,ClientsContact

# Register your models here.
admin.site.register(ClientsProfile)
admin.site.register(DesignationMasterNew)
admin.site.register(RolesMasterNew)
admin.site.register(ClientsTeam)
admin.site.register(ClientsContact)

