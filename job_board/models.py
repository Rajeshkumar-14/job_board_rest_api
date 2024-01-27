from django.db import models


class JobBoard(models.Model):
    job_title = models.CharField(max_length=150)
    job_description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title | str(self.salary)