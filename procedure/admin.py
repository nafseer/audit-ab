from django.contrib import admin
from .models import ProcedureMaster,ProcedureComments,ProcedureFile
# Register your models here.
admin.site.register(ProcedureMaster)
admin.site.register(ProcedureComments)
admin.site.register(ProcedureFile)
