from django.http import JsonResponse, HttpRequest
import json

from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError

from blog.models import Post
from blog.schemas import PostListSchema, PostSchema, PostCreateSchema


@csrf_exempt
def post_list(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        posts = Post.objects.all()
        response = PostListSchema(posts=list(posts))
        return JsonResponse(response.model_dump())

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            post = PostCreateSchema.model_validate(data)

            new_post = Post.objects.create(**post.model_dump())
            response = PostSchema.model_validate(new_post)
            return JsonResponse(response.model_dump())
        except ValidationError as e:
            return JsonResponse(e.errors(), status=400, safe=False)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': "Invalid Json"}, status=400)

    else:
        return JsonResponse({'error': "Method not allowed"}, status=405)


def post_detail(request: HttpRequest, post_id: int) -> JsonResponse:
    try:
        post = Post.objects.get(id=post_id)
        response = PostSchema.model_validate(post)
        return JsonResponse(response.model_dump())
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)