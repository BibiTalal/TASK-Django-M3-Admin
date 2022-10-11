from django.contrib import admin

from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display=("id","name","hp","active",)
    list_filter=("active",)
    list_display_links=("id","name",)
    readonly_fields=("created_at","modified_at",)

    fieldsets=(
        ("general",{
           "fields":("name","type","hp","active",)
        }),

        ("localizations",{
             "fields":("name_fr","name_ar","name_jp",)
        }),


    )

