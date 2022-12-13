from django.urls import path
from .views import blog, info, api


urlpatterns = [
    path('blog/', blog, name='blog'),
    path('info/',info, name='info'),
    path('api/',api, name='api'),
]
