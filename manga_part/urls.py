from django.urls import path
from manga_part.views import GenreView
from manga_part.views import TypeOfMangaView
from manga_part.views import MangaView
from manga_part.views import AddComment
from manga_part.views import CommentView




urlpatterns = [
    path('api/v1/genres/', GenreView.as_view({"get":"list"})),
    path('api/v1/type/', TypeOfMangaView.as_view({"get":"list"})),
    path('api/v1/manga/', MangaView.as_view({"get":"list"})),
    path('api/v1/comment/',CommentView.as_view({"get":"list"})),
    path('api/v1/add_comment/<int:post>/', AddComment.as_view({"post":"create"})),

]