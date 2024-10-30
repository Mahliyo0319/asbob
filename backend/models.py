from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.templatetags.static import static
# Create your models here.



class Header_slider(models.Model):
    min_title=models.CharField(max_length=25)
    title=models.CharField(max_length=25)
    
    img=models.ImageField(upload_to='header_img/%y.%m.%d')
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title



class Models(models.Model):
    name=models.CharField(max_length=40)

    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='Main_Model'
        ordering=['name']
        verbose_name='Model'
        verbose_name_plural='Models'
        unique_together=('name',)




    def __str__(self) -> str:
        return self.name





class Brand(models.Model):
    name=models.CharField(max_length=40)
    img=models.ImageField()
    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table='Main_Brand'
        ordering=['name']
        verbose_name='Brand'
        verbose_name_plural='Brands'
        unique_together=('name',)




    def __str__(self) -> str:
        return self.name
    


class Category(models.Model):
    name=models.CharField(max_length=40)

    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='Main_Category'
        ordering=['name']
        verbose_name='Category'
        verbose_name_plural='Categorys'
        unique_together=('name',)



class Product(models.Model):
    Colors=[
        ("Red","Red"),
        ("Green","Green"),
        ("Whit","Whit"),
        ("Black","Black"),
        
    ]
    Size=[
        ('s','s'),
        ('l','l'),
        ('xs','xs'),
        ('xl','xl'),
        ('m','m')
    ]
    Availability=[
        ("available","Availability"),
         ('unavailable','Unavailabile')
    ]
    name=models.CharField(max_length=80)
    price=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
    producte_tags=models.TextField(max_length=300)
    size=models.CharField(max_length=15,choices=Size)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE, default=None)
    description=models.TextField(max_length=1000)
    image = models.ImageField(upload_to='products/products_img')
    image_preview_small = models.ImageField(upload_to='products/products_img/preview/small/', null=True, blank=True)
    image_preview_medium = models.ImageField(upload_to='products/products_img/preview/medium/', null=True, blank=True)
    image_preview_large = models.ImageField(upload_to='products/products_img/preview/large/', null=True, blank=True)
    selling_count=models.PositiveBigIntegerField()
    review=models.PositiveBigIntegerField()
    rating=models.PositiveIntegerField()
    madel=models.ForeignKey(Models,on_delete=models.CASCADE)
    color=models.CharField(choices=Colors,max_length=15)
    wishlist=models.BooleanField(default=False)
    amount=models.PositiveBigIntegerField(default=0)
    availability = models.CharField(choices=Availability, max_length=30, default="available")
    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='Main_Product'
        ordering=['selling_count','price', 'rating']
        verbose_name='Product'
        verbose_name_plural='Products'
        unique_together=('name','madel')




    def __str__(self) -> str:
        return self.name

    def Rate(self):
        if self.rating:
            hole_star=5-self.rating
            return mark_safe('<img src="%s" width="30" />' %  static('assets/images/icons/img.jpg')*self.rating+ '<img src="%s" width="30" />' %  static('assets/images/icons/images.jpg')*hole_star)
