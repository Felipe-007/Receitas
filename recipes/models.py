# tabela de dados
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name  # faz aparece o nome da categoria


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    # category = faz a relação emtre caregoria e as receitas
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title  # faz aparece o nome da receita


# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)

# auto_now =  atualiza a data toda vez que o objeto é modificado.
# auto_now_add = atualiza a data apenas na criação do objeto.
