import uuid
from django.db import models
from django.utils import timezone

class Ticket(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	autor = models.ForeignKey('auth.User')
	########tecnico = models.ForeignKey('tec.User', blank=True, null=True)
	#titulo = models.CharField(max_length=200)
	descripcion = models.TextField()
	#notas = models.TextField()
	#solucion = models.TextField()
	fecha_creación = models.DateTimeField(default=timezone.now)
	#fecha_cierre = models.DateTimeField(blank=True, null=True)
	prioridad = (
		('Ba', 'Baja'),
		('Me', 'Media'),
		('Al', 'Alta'),
		('Gr', 'Grave'),
		('Cr', 'Crítica'),
	)
	estado = (
		('I', 'Inicio'),
		('A', 'Asignado'),
		('P', 'En_proceso'),
		('C', 'Cerrada'),
	)

	"""def cerrar(self):
		self.fecha_cierre = timezone.now()
		self.save()"""

	def __str__(self):
		return self.autor

