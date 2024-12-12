from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from datetime import datetime


class MyForm(models.Model):
    user_email = models.EmailField(
        verbose_name='Email',
        validators=[EmailValidator()]
    )

    user_phone = models.CharField(
        verbose_name='Phone',
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
            message='Номер телефона задается в формате: +7 xxx xxx xx xx'
        )]
    )

    order_date = models.DateField(
        verbose_name='Order Date',
        null=True, blank=True
    )

    lead_text = models.TextField(
        verbose_name='Lead Text',
        null=True, blank=True
    )

    def __str__(self):
        return self.user_email


from django.db import models

class Feedback(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    order_date = models.DateField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.email
