from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Song,Playlist

@receiver(pre_delete, sender=Song)
def delete_files(sender, instance, **kwargs):
    # Image dosyasını sil
    if instance.image:
        instance.image.delete(save=False)
    # Audio dosyasını sil
    if instance.audio_file:
        instance.audio_file.delete(save=False)

@receiver(pre_delete, sender=Playlist)
def delete_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)