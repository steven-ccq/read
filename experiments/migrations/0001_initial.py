# Generated by Django 2.2.6 on 2020-03-27 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(default='media/book/1.JPG', upload_to='media/book', verbose_name='封面')),
                ('title', models.CharField(max_length=50, verbose_name='书名')),
                ('writer', models.CharField(max_length=50, verbose_name='作者')),
                ('publish_house', models.CharField(max_length=100, verbose_name='出版社')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='出版日期')),
                ('page', models.IntegerField(verbose_name='页数')),
                ('price', models.IntegerField(verbose_name='定价')),
                ('star', models.FloatField(default=5, verbose_name='评分')),
                ('people', models.IntegerField(default=0, verbose_name='评分人数')),
                ('summary', models.TextField(max_length=500, verbose_name='简介')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='评论人')),
                ('image', models.ImageField(default='madia/user/1.JPG', upload_to='', verbose_name='头像')),
                ('comment', models.TextField(max_length=200, verbose_name='评论')),
                ('book_id', models.IntegerField(verbose_name='书的id')),
                ('cover', models.ImageField(default='media/book/1.JPG', upload_to='', verbose_name='封面')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('grade', models.IntegerField(default=5, verbose_name='评分')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('book_id', models.IntegerField(verbose_name='书的id')),
                ('cover', models.ImageField(default='media/book/1.JPG', upload_to='', verbose_name='封面')),
                ('mark', models.IntegerField(choices=[(0, '想读'), (1, '在读'), (2, '读过')], verbose_name='标记')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(default='111111', max_length=150, verbose_name='密码')),
                ('image', models.ImageField(default='madia/user/1.JPG', upload_to='media/user', verbose_name='头像')),
                ('is_online', models.IntegerField(choices=[(0, '未登录'), (1, '已登录')], default=0, verbose_name='状态')),
            ],
        ),
    ]
