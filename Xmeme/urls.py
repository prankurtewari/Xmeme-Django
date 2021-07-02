from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My great API', url='/a-different-path')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    #url(r'^docs/', schema_view),
    path('', include('frontend.urls')),
]