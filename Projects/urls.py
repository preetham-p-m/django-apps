
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Projects.rootappurls')),
    path('calculator/', include('Calculator.urls')),
    path('voting/', include('Voting.urls')),
]
