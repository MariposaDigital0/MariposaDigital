from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(Role)
admin.site.register(TeamMember)
