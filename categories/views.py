from django.db.models import Count
from django.shortcuts import (
    render, get_object_or_404, get_list_or_404)
from django.http import JsonResponse

from dal import autocomplete

from .models import (
    Sector, Qualification, Unit,
    KnowledgeStatement, SkillStatement)


# Autocompletes

class QualificationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Qualification.objects.order_by('name')

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class UnitAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Unit.objects.none()

        qualification = self.forwarded.get('qualification', None)

        if qualification:
            qs = Unit.objects.order_by('pk')
            qs = qs.filter(qualification=qualification)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class KnowledgeStatementAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = KnowledgeStatement.objects.none()

        qualification = self.forwarded.get('qualification', None)
        unit = self.forwarded.get('unit', None)

        if qualification:
            qs = qs.filter(qualification=qualification)

        if unit:
            qs = KnowledgeStatement.objects.order_by('pk')
            qs = qs.filter(unit=unit)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


# AJAX
# NOT USED FOR NOW

def sector_list(self):
    sectors = Sector.objects.order_by('pk')
    data = {"results": list(sectors.values("pk", "name"))}
    return JsonResponse(data)

def qualification_list(self):
    qualifications = Qualification.objects.order_by('pk')
    data = {"results": list(qualifications.values("pk", "name"))}
    return JsonResponse(data)

def unit_list(self):
    units = Unit.objects.order_by('pk')
    data = {"results": list(units.values("pk", "name"))}
    return JsonResponse(data)

def knowledge_statement_list(self):
    kss = KnowledgeStatement.objects.order_by('pk')
    data = {"results": list(kss.values("pk", "name"))}
    return JsonResponse(data)

def skill_statement_list(self):
    sss = SkillStatement.objects.order_by('pk')
    data = {"results": list(sss.values("pk", "name"))}
    return JsonResponse(data)
