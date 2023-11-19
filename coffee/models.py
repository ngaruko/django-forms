from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Flavour(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)


