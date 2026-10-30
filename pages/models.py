from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page


class PrestationsPage(Page):
    introduction = RichTextField(blank=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        InlinePanel ("prestations", label="Prestations"),

    ]

class Prestation(Orderable):
    page = ParentalKey(PrestationsPage, on_delete=models.CASCADE, related_name="prestations",
    )
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2)

    panels = [
        FieldPanel("nom"),
        FieldPanel("description"),
        FieldPanel("prix"),
    ]

class EquipePage(Page):
    image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",)

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        InlinePanel("membres", label="Membres de l'équipe")
    ]

class MembreEquipe(Orderable):
    page = ParentalKey(EquipePage, on_delete=models.CASCADE, related_name="membres")
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    panels = [
        FieldPanel("nom"),
        FieldPanel("description"),
    ]



class ContactPage(Page):
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("adresse"),
        FieldPanel("telephone"),
        InlinePanel("horaires", label="Horaires d'ouverture"),
    ]


class Horaire(Orderable):
    # une ligne d'horaire, reliée à la page Contact
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name="horaires",
    )
    jours = models.CharField(max_length=100)
    heures = models.CharField(max_length=100)

    panels = [
        FieldPanel("jours"),
        FieldPanel("heures"),
    ]

