from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=10)


class Document(models.Model):
    uploaded_file = models.FileField(upload_to='images/')
    expiration_date = models.DateField()
    expired = models.BooleanField(default=False)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)