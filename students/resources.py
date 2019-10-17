from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from categories.models import Qualification, Unit

from .models import Student


class StudentResource(resources.ModelResource):
    qualification = fields.Field(
        attribute='qualification',
        column_name='qualification',
        widget=ForeignKeyWidget(Qualification, 'code'))
    units = fields.Field(
        attribute='units',
        column_name='units',
        widget=ManyToManyWidget(Unit,field='code'))
    past_units = fields.Field(
        attribute='past_units',
        column_name='past_units',
        widget=ManyToManyWidget(Unit, field='code'))

    class Meta:
        model = Student
