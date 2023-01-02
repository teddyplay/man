from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from manga_part.models import Genre
from manga_part.models import Manga
from manga_part.models import Type_of_manga
from manga_part.models import Comment
from manga_part.serializers import GenresSerializer
from manga_part.serializers import TypeOfMangaSeializer
from manga_part.serializers import MangaSerializer
from manga_part.serializers import CommentSerializer
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets



class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer





class TypeOfMangaView(viewsets.ModelViewSet):
    queryset = Type_of_manga.objects.all()
    serializer_class = TypeOfMangaSeializer



class MangaView(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer




class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




class AddComment(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        AllowAny,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]
    # def Post(self, request, pk):
    #     post = get_object_or_404(Manga, pk=pk)
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(post=post)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def Post(self, request, pk):
        post = Manga.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post, author=self.request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


