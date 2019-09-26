from django.db import models
import bcrypt
import re


class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_invalid'] = "email is invalid"
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email_unique'] = "email is already registered"
        if len(User.objects.filter(username=postData['username'])) > 0:
            errors['username_unique'] = "username is taken"
        if len(postData['username']) < 2:
            errors['username_length'] = "username must be at least 2 characters"
        if not postData['password'] == postData['confirm_password']:
            errors['password_match'] = "passwords do not match"
        if len(postData['password']) < 6:
            errors['passsword_length'] = "password must be at least 6 characters"
        return errors

    def add_user(self, postData):
        User.objects.create(
            username=postData['username'],
            email=postData['email'],
            pw_hash=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        )

    def login(self, postData):
        user = User.objects.filter(username=postData['username'])
        if user:
            logged_user = user[0]
            return bcrypt.checkpw(postData['password'].encode(), logged_user.pw_hash.encode())


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
