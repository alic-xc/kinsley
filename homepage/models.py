from django.db import models
from django.urls import reverse
# Create your models here.


class Question(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    cough = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    shaking_chills = models.BooleanField(default=False)
    fast_heartbeat = models.BooleanField(default=False)
    nausea = models.BooleanField(default=False)
    vomiting = models.BooleanField(default=False)
    muscle_pain = models.BooleanField(default=False)
    cyanosis = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    pneumonia_point = models.FloatField(default=0.0)
    is_pneumonia_patient = models.BooleanField(default=False)
    xray_scan = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def get_question_result(self):
        count = 0

        if self.cough:
            count += 1

        if self.fever:
            count += 1

        if self.shaking_chills:
            count += 1

        if self.fast_heartbeat:
            count += 1

        if self.nausea:
            count += 1

        if self.vomiting:
            count += 1

        if self.muscle_pain:
            count += 1

        if self.cyanosis:
            count += 1

        if self.headache:
            count += 1

        if count <= 3:
            return {'msg': 'Not a pnenmonia', 'code': 1}

        elif count > 3 and count <= 5:
            return {'msg': 'Might likely be a pnenmonia', 'code': 2}

        elif count > 5 and count <= 7:
            return {'msg': 'Much of a pnemonia', 'code': 3}

        elif count > 7:
            return {'msg': 'A pnenmonia', 'code': 4}

    def get_absolute_url(self):
        return reverse('question_details', kwargs={'pk': self.pk})