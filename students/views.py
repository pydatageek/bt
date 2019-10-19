from dal import autocomplete

from .models import Student


class StudentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Student.objects.none()

        qualification = self.forwarded.get('qualification', None)

        if qualification:
            qs = Student.objects.order_by('-pk')
            qs = qs.filter(qualification=qualification)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
