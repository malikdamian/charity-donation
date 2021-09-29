from pomagam_app.models import Institution


def institution(request):
    return {'institutions': Institution.objects.all().order_by('type')}
