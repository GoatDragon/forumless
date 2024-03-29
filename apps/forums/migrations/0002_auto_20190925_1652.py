# Generated by Django 2.2.5 on 2019-09-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvoters',
            field=models.ManyToManyField(related_name='downvoted', to='users.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='upvoters',
            field=models.ManyToManyField(related_name='upvoted', to='users.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
