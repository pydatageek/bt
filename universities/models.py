from django.db import models

from categories.models import Qualification, Unit


class University(models.Model):
    """
      Each university has one or more qualifications.
    """
    title = models.CharField(max_length=100)
    qualifications = models.ManyToManyField(
        Qualification, related_name='qualifications')

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.title


# TODO: It is needed to be a onepage UnitPrice model
# One university's all qualifications and units should be listed on one page
# to edit!
class UnitPrice(models.Model):
    # TODO: This model OR its view should be changed according to above condition.
    university = models.ForeignKey(
        University, on_delete=models.CASCADE, related_name='unit_prices')
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='unit_prices')
    price = models.DecimalField(max_digits=7, decimal_places=2)
