from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} | month price: {self.price} '

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])
    def __str__(self):
        return f'Plan type: {self.plan_type} | discount: {self.discount_percent} %'

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscription', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscription', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscription', on_delete=models.PROTECT)

    def __str__(self):
        return f'Service: {self.service.name} | Client: {self.client.company_name} | Plan: {self.plan.plan_type}'