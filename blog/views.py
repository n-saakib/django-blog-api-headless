from django.http import JsonResponse

from blog.schemas import MessageResponse


def hello_api(request):
    response = MessageResponse(message="Hello, World!")
    return JsonResponse(response.model_dump())