from django.db import models


class WebsiteType(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)

    def __str__(self):
        return f"({self.id}) {self.title}"


class WebsiteSignature(models.Model):
    domain = models.CharField(max_length=256, null=False, unique=True)
    type = models.ForeignKey(WebsiteType, on_delete=models.SET_NULL, null=True)
    accessed = models.BooleanField(default=True)

    def __str__(self):
        return f"({self.id}) {self.domain}"