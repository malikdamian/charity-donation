from django.contrib import admin
from pomagam_app.models import Institution, Donation, Category


@admin.register(Institution)
class AdminInstitution(admin.ModelAdmin):
    pass


@admin.register(Donation)
class AdminDonation(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass
