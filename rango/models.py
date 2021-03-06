from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_online = models.BooleanField(default=False)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_image', blank=True)



    def __str__(self):
        return self.user.username

class Friends(models.Model):
    user = models.ForeignKey(User)
    friend_id = models.IntegerField()
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(User.objects.get( pk = int(self.friend_id)))

class Userremove(models.Model):
    groupone = models.CharField(null=True, max_length=50)
class Useradd(Userremove):
    grouptwo = models.CharField(null=True, max_length=50)



