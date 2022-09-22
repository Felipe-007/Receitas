from django.test import TestCase
from django.urls import reverse, resolve  #resolve resolve qual função esta sendo usada por uma url # noqa
from recipes import views


class RecipeURLsTest(TestCase):
    """ def test_the_pytest_is_ok(self):
        assert 1 == 1, 'os números são iguais' """

    def test_home_url_is_correct(self):
        url = reverse('recipes:home')  # pega o urls.py de recipes
        self.assertEqual(url, '/')  # testa a pagina principal

    def test_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})  # pega o urls.py de recipes # noqa
        self.assertEqual(url, '/recipes/category/1/')  # testa o category

    def test_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')  # testa o detalhes


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
