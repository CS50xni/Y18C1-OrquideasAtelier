from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


class ProductManager(models.Manager):
    def all(self, **kwargs):
        return self.get_queryset().filter(active=True, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True )
    price = models.DecimalField(decimal_places=2, max_digits=6, default=10.00)
    created_at = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    time = models.PositiveIntegerField(null=True)#Days to make the product
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    #Product manager
    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
    
    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'slug': self.slug, 'id': self.id})
        #return "/products/{slug}-{id}/".format(slug=self.slug,id=self.id)

    def get_image_url(self):
        img = self.productimage_set.first()
        return img.image.url if img else img

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='products/', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.title


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True, unique=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs=(self.slug))


#slug Generator
def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)