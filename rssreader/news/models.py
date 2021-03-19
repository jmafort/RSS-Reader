from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, null=False, unique=True)
    full_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=64, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id}: {self.username}"

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=64)
    channel_url = models.URLField(null=False)

    def __str__(self):
        return f"{self.channel_id}: {self.display_name} {self.channel_url}"

class Userchannel(models.Model):
    userchannel_id = models.AutoField(primary_key=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.userchannel_id}: Usuário: {self.user.username} | Canal: {self.channel.display_name} | Favorito? {'Sim' if self.is_favorite else 'Não'}"