from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ordering = models.IntegerField(null=False, unique=True, blank=False)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False);

    def __str__(self):
        return self.title
