from django.shortcuts import render_to_response, redirect
from openkansas_api.models import District
# Create your views here.

def handle_query(request):
    if not request.GET.has_key('q'):
        return redirect('openkansas_api_index')

    (geodata, object_list) = District.objects.by_geocode(request.GET['q'])
    return render_to_response('openkansas_api/list.html', {
        'object_list': object_list,
    })

def handle_index(request):
    return render_to_response('openkansas_api/search.html')

def handle_details(request, type, district, *args):
    real_type = type[0:3].upper()
    district = District.objects.get(type = real_type, district = district)
    return render_to_response('openkansas_api/details.html', {
        "district": district,
    })
