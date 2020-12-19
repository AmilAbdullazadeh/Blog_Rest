from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from comment.api.views import (
    CommentListAPIView,
    # PostDetailAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
    CommentCreateAPIView
)

app_name = "comment"

urlpatterns = [
                  path('list', CommentListAPIView.as_view(), name='list'),
                  # path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
                  path('delete/<pk>', CommentDeleteAPIView.as_view(), name='delete'),
                  path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),
                  path('create/', CommentCreateAPIView.as_view(), name='create'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
