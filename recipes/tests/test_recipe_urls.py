from django.test import TestCase
from django.urls import reverse


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