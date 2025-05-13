from django.db import models
from django.utils import timezone
class Bot(models.Model):
    Id_Bot = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250)
    Token = models.CharField(max_length=250)
    Numero = models.CharField(max_length=50, null=True)
    Activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  # Asigna la fecha y hora actuales por defecto
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Bots"


class FAQ(models.Model):
    Id_FAQ = models.AutoField(primary_key=True)
    Pregunta = models.CharField(max_length=500)
    Respuesta = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "FAQS"


class Anuncio(models.Model):
    Id_Anuncio = models.AutoField(primary_key=True)
    Id_Bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=250)
    Contenido = models.TextField()
    Fecha = models.DateField()
    Activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Anuncios"


class Usuario(models.Model):
    Id_Usuario = models.AutoField(primary_key=True)
    Id_Chat = models.BigIntegerField()
    Usuario = models.CharField(max_length=150)
    Activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Usuarios"


class Solicitud_Bot(models.Model):
    Id_Solicitud = models.AutoField(primary_key=True)
    Id_Bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    Id_FAQ = models.ForeignKey(FAQ, on_delete=models.CASCADE, null=True)
    Id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Consulta = models.TextField()
    Respuesta = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Solicitudes_Bot"


class Accion(models.Model):
    Id_Accion = models.AutoField(primary_key=True)
    Id_Solicitud = models.OneToOneField(Solicitud_Bot, on_delete=models.CASCADE)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Plataforma = models.CharField(max_length=100)
    Accion = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Acciones"


class Carrera(models.Model):
    Id_Carrera = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Facultad = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Carreras"


class Estudiante(models.Model):
    Id_Estudiante = models.AutoField(primary_key=True)
    Id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Semestre = models.IntegerField()
    Telefono = models.CharField(max_length=50)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Estudiantes"


class Materia(models.Model):
    Id_Materia = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=150)
    Descripcion = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Materias"


class Docente(models.Model):
    Id_Docente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Docentes"


class Materia_Ofertada(models.Model):
    Id_Materia_Ofertada = models.AutoField(primary_key=True)
    Semestre = models.IntegerField()
    Fecha_Inicio = models.DateField()
    Fecha_Final = models.DateField()
    Id_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Id_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    Modulo = models.CharField(max_length=50)
    Año = models.IntegerField()
    Activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Materia_Ofertadas"


class Inscripcion(models.Model):
    Id_Inscripcion = models.AutoField(primary_key=True)
    Id_Materia = models.ForeignKey(Materia_Ofertada, on_delete=models.CASCADE)
    Id_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Inscripciones"

class Recomendacion(models.Model):
    Id_Recomendacion = models.AutoField(primary_key=True)
    Id_Bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    Recomendacion = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
