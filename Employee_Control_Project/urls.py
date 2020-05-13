from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
	path('', include('project_crud.urls')),
	path('project_crud/', include('project_crud.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico'))
]


