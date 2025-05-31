from django.db import models
from searchApp.models import *



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, default='Nome completo')
    birthday = models.DateField(default=None, null=True, blank=True)
    civil_status = models.IntegerField(choices=STATUS_CHOICES, default=5)
    address = models.CharField(default='Rua, nº, freguesia, Código Postal')
    education = models.IntegerField(choices=EDUCATION_CHOICES, default=4)
    health_informations = models.TextField(default='Descreva sobre o seu atual quadro de obesidade, quais as medicações que faz uso e se possui outras doenças crônicas')
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #image = models.ImageField(null=True, blank=True)



    #addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')


"""
    def __str__(self):
        return '{}'.format(self.user.username)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):

        try:
            instance.profile.save()

        except:
            pass

"""



