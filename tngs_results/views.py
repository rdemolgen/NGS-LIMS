from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Sample_list

# Create your views here.

def post_list(request):
    patient_sample_list = Sample_list.objects.order_by('ex_number')
    return render(request, 'tngs_results/index.html', { 'patient_sample_list': patient_sample_list})
#why recall something as something else? call it a name that makes sense from the start

#def index(request):
#    return HttpResponse("Hello, this is the tng_results homepage, enter patient id")

#def detail(request, patient_id):
    #insert igv.js
#    return HttpResponse("you're looking at patient details  for %s." %patient_id)
