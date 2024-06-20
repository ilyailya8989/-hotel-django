from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Room(models.Model):
    numbers = models.IntegerField(default=1)
    classification = models.CharField(max_length=100)
    priceOnNight = models.IntegerField(default=50)
    description = models.TextField()
    rooms = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)


    def __str__(self):
        return f'номер комнаты {self.numbers}.{self.classification}'



