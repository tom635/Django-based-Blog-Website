from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page.as_view(), name="starting-page"),
    path("posts", views.posts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.post_detail.as_view(),
         name="post-detail-page"),  # /posts/my-first-post,
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]