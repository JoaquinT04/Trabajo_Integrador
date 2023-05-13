from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	dni = models.PositiveIntegerField()

	def __str__(self) -> str:
		return f"{self.nombre} {self.apellido} {self.dni}"
	
	class Meta:
		ordering = ["apellido","nombre","dni"]