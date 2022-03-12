from django.contrib import admin
from apps.home.models import Home, Service, Partners, Price, Team, FAQ


admin.site.register(Home)
admin.site.register(Service)
admin.site.register(Price)
admin.site.register(Partners)
admin.site.register(Team)
admin.site.register(FAQ)