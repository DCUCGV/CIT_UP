from django.urls import path,include, re_path
from . import views
app_name = 'app_DRF_start'

urlpatterns = [
    # path('',include('rest_framework.urls',namespace='rest_framework_category')),
    path('',views.sensor_view, name = 'sensor_view'),
]