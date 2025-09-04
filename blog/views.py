from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def post_list(request: Request) -> Response:
    if request.method == 'GET':
        posts = Post.objects.all()
        response = PostSerializer(posts, many=True)
        return Response(response.data)

    elif request.method == 'POST':
        data = PostSerializer(data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def post_detail(request: Request, post_id: int) -> Response:
    try:
        post = Post.objects.get(id=post_id)
        response = PostSerializer(post)
        return Response(response.data)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)