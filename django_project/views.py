from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def welcome_view(request):
    """
    A simple welcome view that returns a greeting message.
    """
    return Response({"message": "Welcome to the Django REST Framework API!"})