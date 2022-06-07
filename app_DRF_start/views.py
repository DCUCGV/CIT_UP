from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework import viewsets
from app_DRF_start.serializers import InfoSerializer
from app_DRF_start.models import Info
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
# from .push_fcm import send_to_firebase_cloud_messaging
from rest_framework.response import Response

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def send_test_volume(request):
#     send_to_firebase_cloud_messaging.delay()
#     return Response({"message":"ok"})
def main(request):
    return render(request, 'app_DRF_start/CGV.html')

def login(request):
    return render(request,'app_DRF_start/CGV_login.html')

def about(request):
    return render(request,'app_DRF_start/CGV_About.html')

def data(request):
    page = request.GET.get('page', '1')
    infos = Info.objects.all()
    paginator = Paginator(infos, 20)
    page_obj = paginator.get_page(page)
    context = {'infos': page_obj}
    return render(request,'app_DRF_start/CGV_Data.html',context)

def mypage(request):
    return render(request,'app_DRF_start/CGV_mypage.html')

def sensor_view(request):
    page = request.GET.get('page', '1')
    infos = Info.objects.all()
    paginator = Paginator(infos, 20)
    page_obj = paginator.get_page(page)
    context = {'infos': page_obj}
    return render(request, 'app_DRF_start/sensorpage.html', context)


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer



