from django.db import models

from accounts.models import User


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)  # ユーザー名
    text = models.TextField()  # 本文
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return f"{self.username}, {self.text}"