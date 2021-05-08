from django.db import models

class Intro(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='intro')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Skill(models.Model):
    icon = models.CharField(max_length=100, verbose_name='FontAwesome Icon', help_text="Font Awesome copy the icon with i tag")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Project(models.Model):
    title = models.CharField(max_length=200)
    short_des = models.CharField(max_length=200)
    github_link = models.URLField(max_length=999999)
    live_dmeo_link = models.URLField(max_length=999999)
    image = models.ImageField(upload_to='project')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class SocialAccount(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, verbose_name='FontAwesome Icon',
                            help_text="Font Awesome copy the icon with i tag")
    link = models.URLField(max_length=999999)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name