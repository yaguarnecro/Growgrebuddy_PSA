# views.py
# This file contains the view functions for the Django application.

from django.http import HttpResponse, JsonResponse

# View for returning an HTML response
def hello_world(request):
    return HttpResponse("Hello World")  # Return a simple HTML response

# API view for returning a JSON response
def hello_world_api(request):
    return JsonResponse({"message": "Hello World"})  # Return a JSON response