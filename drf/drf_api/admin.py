from django.contrib import admin

from . import models

# v2
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.AuthorDetail)
admin.site.register(models.Car)