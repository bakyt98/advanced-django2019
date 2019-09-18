from article.models import Company, Article
from django.contrib.auth.models import User
from django.test import TestCase


class CompanyTest(TestCase):
    def setUp(self):
        Company.objects.create(name='EGOV')
        Company.objects.create(name='ArticleReport')

    def test_company_str(self):
        egov = Company.objects.get(name='EGOV')
        artreport = Company.objects.get(name='ArticleReport')
        self.assertEqual(egov.__str__(), "EGOV")
        self.assertEqual(artreport.__str__(), "ArticleReport")


class ArticleTest(TestCase):
    def setUp(self):
        egov = Company.objects.create(name='EGOV')
        author = User.objects.create(username='bakyt',
                                     email='isimovabakyt@gmail.com',
                                     password='ghbdtn1234')
        Article.objects.create(title='Waterpost', rating=4,
                               summary='djfvjnadvk;oafjnv',
                               ip_address='127.0.0.4',
                               submission_date='2017-07-15',
                               company=egov, reviewer=author)

    def test_article_str(self):
        article = Article.objects.get(title='Waterpost')
        self.assertEqual(article.__str__(), ("{} Waterpost").format(str(article.id)))  # noqa
