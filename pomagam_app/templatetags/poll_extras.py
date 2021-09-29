from django.db.models import Sum
from django import template

from pomagam_app.models import Donation

register = template.Library()


@register.simple_tag
def get_total_bags_num():
    return Donation.objects.all().aggregate(total_bags=Sum('quantity'))['total_bags']


@register.simple_tag
def get_total_bags_user():
    return Donation.objects.filter(pk=13).aggregate(total_bags=Sum('quantity'))['total_bags']