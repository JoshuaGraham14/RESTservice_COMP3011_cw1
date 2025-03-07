from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    professor_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return f"{self.professor_id}, {self.name}"

class Module(models.Model):
    module_code = models.CharField(max_length=10, unique=True) 
    name = models.CharField(max_length=255, unique=False) 

    def __str__(self):
        return f"{self.module_code}, {self.name}"

class ModuleInstance(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="instances")
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.module.name} ({self.year} - Semester {self.semester})"

class ProfessorModule(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(ModuleInstance, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professor.name} teaches {self.module_instance}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(ModuleInstance, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username} rated {self.professor.name} {self.rating} stars"
