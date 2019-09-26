from django.db import models
from apps.users.models import User


class PostManager(models.Manager):
    def validate(self, postdata):
        pass

    def create_post(self, postdata, author, parent=None):
        newpost = Post.objects.create(
            parent=parent,
            author=author,
            title=postdata['title'],
            contents=postdata['contents'],
            votes=1
        )
        newpost.upvoters.add(author)

    def delete_post(self, postdata):
        pass

    def edit_post(self, postdata):
        pass

    def vote(self, user_id, vote, post_id):
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        if vote == 1:
            if user in post.downvoters.all():
                post.upvoters.add(user)
                post.downvoters.remove(user)
                post.votes += 2
                post.save()
            elif user in post.upvoters.all():
                post.upvoters.remove(user)
                post.votes -= 1
                post.save()
            else:
                post.upvoters.add(user)
                post.votes += 1
                post.save()
        if vote == -1:
            if user in post.downvoters.all():
                post.downvoters.remove(user)
                post.votes += 1
                post.save()
            elif user in post.upvoters.all():
                post.upvoters.remove(user)
                post.downvoters.add(user)
                post.votes -= 2
                post.save()
            else:
                post.downvoters.add(user)
                post.votes -= 1
                post.save()


class Post(models.Model):
    parent = models.ForeignKey('self', related_name="children", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, null=True)
    contents = models.TextField()
    votes = models.IntegerField()
    upvoters = models.ManyToManyField(User, related_name="upvoted")
    downvoters = models.ManyToManyField(User, related_name="downvoted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
