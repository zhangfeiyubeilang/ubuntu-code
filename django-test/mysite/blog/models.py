from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
#加外键时，需要加上on_delete=models.CASCADE,否则数据迁移时出错
class BlogArticle(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ("-publish",)#必须是元组类型

    def __str__(self):
        return self.title