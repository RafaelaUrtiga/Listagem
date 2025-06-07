import uuid
from django.db import models




class Clients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=65)
    card_number = models.IntegerField()
    born_in = models.DateField()
    
    address = models.CharField(max_length=165)
    number = models.CharField(max_length=10, blank=True)
    complement = models.CharField(max_length=100, blank=True)
    #slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True) # data no momento da criação
    updated_at = models.DateTimeField(auto_now=True) # data no momento da atualização quando salvar
    active = models.BooleanField(default=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='cadastro/photos/%Y/%m/%d')
    archived_at = models.DateTimeField(null=True, blank=True)
    archived_by = models.ForeignKey(
        #User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assistidos_arquivados'
    )

