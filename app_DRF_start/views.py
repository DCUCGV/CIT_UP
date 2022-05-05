from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework import viewsets
from app_DRF_start.models import Info
from app_DRF_start.serializers import InfoSerializer

# Create your views here.
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
