from django.http import JsonResponse
def myview(request):
    json_response = {"message" : "Hello World!"}
    return JsonResponse(json_response)
# Create your views here
