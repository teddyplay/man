from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from manga_part.models import Manga
from manga_part.models import Type_of_manga
from manga_part.models import Genre
from manga_part.models import Comment
from users.models import User

class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=2,
                                     max_length=20,
                                     )

    class Meta:
        model = User
        fields = ["username"]



class GenresSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(min_length=3,
                                   max_length=50,
                                   )

    class Meta:
        model = Genre
        fields = ['id',
                  'genre',
                  ]



class TypeOfMangaSeializer(serializers.ModelSerializer):
    type_of = serializers.CharField(min_length=1,
                                 max_length=50,
                                 )


    class Meta:
        model = Type_of_manga
        fields = ["id",
                  "type_of",
                  ]





class MangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1,
                                 max_length=70,
                                 )
    year = serializers.IntegerField(default=0,
                                    )


    class Meta:
        model = Manga
        fields = ["id",
                  "name",
                  "year",
                  ]


class CommentSerializer(serializers.ModelSerializer):
    username_id = AuthorSerializer(read_only=True)
    text = serializers.CharField(max_length=500, required=False)
    # extra_kwargs = {"username_id": {"read_only": True}}

    class Meta:
        model = Comment
        fields = ["id",
                  "text",
                  "username_id",
                  # "manga_id",
                  ]



