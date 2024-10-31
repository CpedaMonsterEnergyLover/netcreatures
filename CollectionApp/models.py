from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    title = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.id}) {self.title}"


class Creature(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    date_created = models.DateTimeField(auto_now_add=True)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.title}"


class CreatureInstance(models.Model):
    date_acquired = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creature = models.ForeignKey(Creature, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.creature.title} of {self.user.username}"


class CreatureEncounter(models.Model):
    STATUSES = (
        ('pending', 'PENDING'),
        ('success', 'SUCCESS'),
        ('failed', 'FAILED')
    )

    creature = models.ForeignKey(Creature, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, default='pending', choices=STATUSES)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.creature.title} encounter for {self.user.username}"

    # 5 minutes auto fail encounter if pending