from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True )
    price = models.DecimalField(decimal_places=2, max_digits=6, default=10.00)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    #TODO
    # Name, Description,Price,Categorie,
    # SKU,created, ...

    #separate product options:
    #Time, color, size,type


    pass

class Category(models.Model):
    #TODO
    #name, description
    pass

class ProductImage(models.Model):
    #TODO
    pass

class Types(models.Model):
    #TODO
    pass
