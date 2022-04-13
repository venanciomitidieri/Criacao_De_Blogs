from django.db import models
from django.db.models import permalink


class Blog(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True)
    corpo = models.TextField()
    data = models.DateField(db_index=True, auto_now_add=True)
    categoria = models.ForeignKey('django_app.Categoria')

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_url_absoluta(self):
        return ('ver_post_blog', None, { 'slug': self.url })


class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    url = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_url_absoluta(self):
        return ('ver_categoria_blog', None, { 'slug': self.url })