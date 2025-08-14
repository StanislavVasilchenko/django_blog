from django.shortcuts import get_object_or_404, render

from publish.models import Post


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.view_count += 1
    post.save()
    return render(
        request,
        "publish/post.html",
        context={"post": post},
    )
