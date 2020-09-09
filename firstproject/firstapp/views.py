from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,AccessRecord,Webpage
# Create your views here.

def index(request):
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':Webpages_list}
    return render(request,'index.html',context=date_dict)