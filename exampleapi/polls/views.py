from django.http import JsonResponse

# Create your views here.
def index(request):
    return JsonResponse({"status" : True, "message" : "hello django!" })

def another(request):
    return JsonResponse({"status" : True, "message" : "hello anoter!" })
