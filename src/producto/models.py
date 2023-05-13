from django.db import models
from proveedor.models import Proveedor
# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	precio= models.FloatField()
	stock_actual = models.IntegerField()
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
	
	def __str__(self) -> str:
		return f"{self.nombre.capitalize} {self.precio} stock: {self.stock_actual}"
	
	class Meta:
		ordering=["stock_actual"]