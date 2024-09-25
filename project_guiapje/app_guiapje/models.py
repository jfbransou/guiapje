from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Paragraph(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='paragraphs')
    text = models.TextField()

    def __str__(self):
        return f'Paragraph in {self.chapter.title}'

class Comment(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Interaction(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='interactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('chapter', 'user')