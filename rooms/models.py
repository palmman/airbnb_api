from django.db import models
from users.models import Account

# Create your models here.


class HostRooms(models.Model):

    owner = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='host')
    name = models.CharField(max_length=499, null=True, blank=True)
    address = models.CharField(max_length=499, null=True, blank=True)
    description = models.TextField()
    room_image = models.ImageField(null=True, blank=True, upload_to='rooms', default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    booking = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):

    owner = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(HostRooms, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
