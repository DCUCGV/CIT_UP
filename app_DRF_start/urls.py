from django.urls import path,include, re_path
from . import views
from . import push_fcm
app_name = 'app_DRF_start'


push_fcm.send_to_firebase_cloud_messaging()
urlpatterns = [
    # path('',include('rest_framework.urls',namespace='rest_framework_category')),
    path('',views.sensor_view, name = 'sensor_view'),
]
