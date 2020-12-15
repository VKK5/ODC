from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from googleplaces import GooglePlaces, types, lang 
#import requests 
#import json  

@api_view(http_method_names= ['GET',])
def Location_list_view(request):
    if request.method == 'GET':
        return Location_list_view_get(request)
    elif request.method == 'POST':
        return Location_list_view_post(request)

def Location_list_view_get(request):
    try:
        form = LocationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                geolocation = latitude+","+longitude
                data = request.get('https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters={}&radius = 1500&type=Doctorskeyword=cruise&key=AIzaSyBrf20NDm-xfD-DWe9_YeupjmcdTRaDa8w'.format(geolocation))

        serializer = LocationDataSerializer(data, many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_406_NOT_FOUND)

def Location_list_view_post(request):
    #enteredBy = request.user
    #hdata = HouseholdData(enteredBy=enteredBy)
    hdata = Location()
    serializer = LocationDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT','DELETE'])
#@permission_classes([IsAuthenticated])
def Location_detail_view(request, slug):

    try:
        hdata = Location.objects.get(username=slug)
        if request.method == 'GET':
            return Location_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return Location_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return Location_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def Location_detail_view_get(request, slug, hdata):
    serializer = LocationDataSerializer(hdata)
    return Response(serializer.data)

def Location_detail_view_put(request, slug, hdata):
    serializer = LocationDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def Location_detail_view_delete(request, slug, hdata):
    #if request.user==hdata.enteredBy:
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    else:
        data = {'message' : 'not same user'}
    return Response(data)
