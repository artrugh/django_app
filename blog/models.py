from django.db import models
from django.urls import reverse


class Post(models.Model):
    # inputs
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=300)

    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()

    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='img')

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s' % self.title

    def get_absolute_url(self):
        return reverse("blog.views.post", args=[self.slug])
