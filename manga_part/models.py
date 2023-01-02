from django.db import models
from users.models import User

class Genre(models.Model):
    genre = models.CharField(max_length=50,
                             verbose_name="Жанр",
                             )



    def __str__(self):
        return self.genre





class Type_of_manga(models.Model):
    type_of = models.CharField(max_length=50,
                             verbose_name="Тип",
                             )


    def __str__(self):
        return self.type_of





class Manga(models.Model):
    name = models.CharField(max_length=60,
                            verbose_name="Название манги",
                            )

    year = models.IntegerField(verbose_name="Год выпуска",
                               )
    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE,
                              )
    type_of_manga = models.ForeignKey(Type_of_manga,
                              on_delete=models.CASCADE,
                              verbose_name="Тип",
                              )


    def __str__(self):
        return self.name





class Comment(models.Model):
    manga = models.ForeignKey(Manga,
                                on_delete=models.CASCADE,


                              )
    text = models.TextField(max_length=400,
                            verbose_name="Комменатрии",
                            )
    username = models.ForeignKey('users.User',
                                 on_delete=models.CASCADE,
                                 )

    # def save(self,*args, **kwargs):
    #     super(Manga,self).save(*args, **kwargs)
    #

    #
    # def __str__(self):
    #     return f'{self.username} прокомменитровал  запись {self.text}'
