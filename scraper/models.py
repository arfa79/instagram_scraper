from django.db import models

class Influencer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    follower_count = models.IntegerField(default=0)

    def str(self):
        return self.username

class Post(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=100, unique=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    def str(self):
        return f"Post by {self.influencer.username} - {self.post_id}"