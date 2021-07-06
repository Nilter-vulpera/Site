from django.db import models
from django.contrib.auth.models import User


#User1 = User.objects.create_user('UserName', 'user@mail.com', 'user_password')


class Author(models.Model):
    name = models.CharField(max_length=200)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    some_datetime = models.DateTimeField()
    many_to_many_relation = models.ManyToManyField(Category)
    Text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    heading = models.CharField(max_length=64, default="Default value")
    position = models.CharField(max_length=2)
    # choices=POSITIONS,
    # default=cashier)


class PostCategory(models.Model):
    one_to_many_relation = models.ForeignKey(Post,on_delete=models.CASCADE)
    one_to_many_relation2 = models.ForeignKey(Category,on_delete=models.CASCADE)


class Comment(models.Model):
    one_to_many_relation = models.ForeignKey(Post,on_delete=models.CASCADE)
    one_to_many_relation1 = models.ForeignKey(User,on_delete=models.CASCADE)
    Text = models.TextField()
    some_datetime = models.DateTimeField()
    rating = models.IntegerField(default=0)