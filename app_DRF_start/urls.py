from django.urls import path,include
from . import views
from . import push_fcm

app_name = 'app_DRF_start'

push_fcm.send_to_firebase_cloud_messaging()
# test_push.send_notification()
# Push.send_to_firebase_cloud_messaging()
urlpatterns = [
    # path('',include('rest_framework.urls',namespace='rest_framework_category')),
    path('main/',views.main, name = 'main'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('data/',views.data,name = 'data'),
    path('mypage/',views.mypage,name='mypage'),
]
