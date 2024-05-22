from django.db import models


class Kind(models.Model):
    image = models.ImageField(upload_to='img/kind')
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='img/item')
    index = models.CharField(max_length = 16)
    description = models.CharField(max_length=256)
    price = models.SmallIntegerField()
    items = models.ForeignKey(Kind, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
