from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category_image = models.ImageField(upload_to="categories", null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)



    def __str__(self) -> str:
        return self.category_name


class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name

class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size_name




class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True  , null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products",null=True,blank=True)
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant , blank=True)
    size_variant = models.ManyToManyField(SizeVariant , blank=True)
    # available=models.BooleanField(default=True) 
    # created=models.DateTimeField(auto_now_add=True)
    # updated=models.DateTimeField(auto_now=True)


    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_name)
        super(Product ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.product_name





class ProductImage(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="product_images")