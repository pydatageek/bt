from django.urls import path

from .views import (
    sector_list, qualification_list, unit_list,
    knowledge_statement_list, skill_statement_list,
    QualificationAutocomplete, UnitAutocomplete,
    KnowledgeStatementAutocomplete)

urlpatterns = [
    path('ac/qualification/', QualificationAutocomplete.as_view(), name='ac_qualification'),
    path('ac/unit/', UnitAutocomplete.as_view(), name='ac_unit'),
    path('ac/ks/', KnowledgeStatementAutocomplete.as_view(), name='ac_ks'),

    # NOT USED FOR NOW
    path('ajax/sector/', sector_list, name='ajax_sector_list'),
    path('ajax/qualification/', qualification_list , name='ajax_qualification_list'),
    path('ajax/unit/', unit_list, name='ajax_unit_list'),
    path('ajax/ks/', knowledge_statement_list, name='ajax_ks_list'),
    path('ajax/ss/', skill_statement_list, name='ajax_ss_list'),
]
