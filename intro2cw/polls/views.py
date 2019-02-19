from django.http import HttpResponse

# call my return to the user
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def gogetthegoods(request):
    return HttpResponse('here you go looking like bobby boshayyyy')



