from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)  # title Post
    content = models.TextField()  # Content of post
    created = models.DateTimeField(auto_now_add=True)  # data and time created post
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # внешний ключ на пользлвателя

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField() # Контент коментария
    created = models.DateTimeField(auto_now_add=True) # дата и время создания коментария
    user = models.ForeignKey(User, on_delete=models.CASCADE) # внешний ключ на полььзвоателя
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # внешний ключ на пост

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


