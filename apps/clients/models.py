from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)

    def __repr__(self):
        return f"<данные клиента: {self.name} {self.surname} {self.phone}>"

