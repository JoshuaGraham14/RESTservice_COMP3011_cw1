from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Module_Instance(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="instances")
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.module.name} ({self.year} - Semester {self.semester})"

class Professor_Module(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(Module_Instance, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professor.name} teaches {self.module_instance}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(Module_Instance, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username} rated {self.professor.name} {self.rating} stars"
