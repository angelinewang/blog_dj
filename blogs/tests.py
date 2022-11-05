from django.test import TestCase
from django.urls import reverse
from .models import Blog

# Create your tests here.

class BlogTestCase(TestCase):
  @classmethod
  def setUpTestData(cls):
        cls.blog = Blog.objects.create(
            title="Amazing Blog",
            description="Best Blog You'll Ever Read",
            content="GooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGoodday",
            author="Angeline",
        )

  def test_blog_content(self):
    self.assertEqual(self.blog.title, "Amazing Blog")
    self.assertEqual(self.blog.description, "Best Blog You'll Ever Read")
    self.assertEqual(
        self.blog.content, "GooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGooddayGoodday")
    self.assertEqual(self.blog.author, "Angeline")

  def test_blog_listview(self):
    response = self.blog.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Angeline")
    self.assertTemplateUsed(response, "blog/blog_list.html")
