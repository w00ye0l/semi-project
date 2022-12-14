from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
from django.conf import settings


class Store(models.Model):
    type_image = (
        ("Grass", "풀"),
        ("Fire", "불"),
        ("Water", "물"),
        ("Lightning", "전기"),
        ("Psychic", "에스퍼"),
        ("Fighting", "격투"),
        ("Darkness", "악"),
        ("Metal", "강철"),
        ("Fairy", "페어리"),
        ("Dragon", "드레곤"),
        ("Colorless", "노말"),
    )

    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="image/", blank=True)
    thumbnail = ProcessedImageField(
        upload_to="image/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 80},
    )
    buysell = models.BooleanField(default=False, null=True)
    cost = models.IntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_store")
    type = models.CharField(max_length=10, choices=type_image)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
