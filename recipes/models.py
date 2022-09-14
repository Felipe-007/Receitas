# tabela de dados
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name  # faz aparece o nome da categoria


class Recipe(models.Model):
    title = models.CharField(max_length=65, verbose_name="Titulo")
    description = models.CharField(max_length=165, verbose_name="Descrição")
    slug = models.SlugField()
    preparation_time = models.IntegerField(verbose_name="Tempo de preparação")
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField(verbose_name="Porções")
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField(verbose_name="Etapas de preparação")
    preparation_steps_is_html = models.BooleanField(
        default=False, verbose_name="Etapas de preparação HTML")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name="Publicado")
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='',
        verbose_name="Imagem")
    # category = faz a relação entre caregoria e as receitas
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        verbose_name="Categoria")

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name="Autor")

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
