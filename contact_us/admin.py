from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'sujet', 'date_creation', 'traite']
    list_filter = ['traite', 'date_creation']
    search_fields = ['nom', 'email', 'sujet']
    readonly_fields = ['date_creation']
    list_editable = ['traite']
    ordering = ['-date_creation']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si on modifie un objet existant
            return self.readonly_fields + ['nom', 'email', 'sujet', 'message']
        return self.readonly_fields