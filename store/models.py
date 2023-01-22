from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories" #zmienia nazwe w panelu admina

    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

class Products(models.Model):

    class Meta:
        verbose_name_plural = "Products" #zmienia nazwe w panelu admina
 
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #on delete kasuje wszystkie produkty z kategorii
    description = models.TextField()
    #image = models.CharField(max_length=300) #mozna dac adres obrazu z google grafika
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title