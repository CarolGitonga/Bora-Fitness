from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.

class PublishedManager(models.Manager):
   def get_queryset(self):
      return super().get_queryset()\
                    .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')#defines many-to-one relationship, each post is written by a user.a user can write any number of posts.a foreign key is created in the database using the primary key of the related model.
    body = models.TextField()
    publish = models.DateTimeField (default=timezone.now) #store the date and time when the post was published
    created = models.DateTimeField(auto_now_add=True) #store the date and time when the post was created.
    updated = models.DateTimeField(auto_now=True) #store the last date and time when the post was updated.
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager()

    """
    Meta class defines metadata for the model.Ordering attribute sorts results by the publish field.
    """

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
       ]
        """
        We have added the indexes option to the model’s Meta class. This option allows you to define database
        indexes for your model, which could comprise one or multiple fields, in ascending or descending
        order, or functional expressions and database functions. We have added an index for the publish
        field. We use a hyphen before the field name to define the index in descending order. The creation of
        this index will be included in the database migrations that we will generate later for our blog models."""

    def __str__(self):#the default python method to return a string with the human-readable representation of the object
         return self.title


    """We have defined the enumeration class Status by subclassing models.TextChoices. The available
    choices for the post status are DRAFT and PUBLISHED. Their respective values are DF and PB, and their
    labels or readable names are Draft and Published."""

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
    #The reverse() function builds the URL dynamically using the URL name defined in the URL patterns.

class Comment(models.Model):
        post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
        name = models.CharField(max_length=80)
        email = models.EmailField()
        body = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)

        class Meta:
            ordering = ['created']
            indexes = [
                models.Index(fields=['created']),
           ]

        def __str__(self):
            return f'Comment by {self.name} on {self.post}'