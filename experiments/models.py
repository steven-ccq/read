from django.db import models
from experiment.settings import *
from django.utils.timezone import now

class User(models.Model):
    name = models.CharField(u'用户名',max_length=50)
    password = models.CharField(u'密码',max_length=150,default='111111')
    image = models.ImageField(u'头像',upload_to='media/user',default='media/user/1.JPG')
    change = (
        (0, "未登录"),
        (1, "已登录")
    )
    is_online = models.IntegerField(u'状态',choices=change,default=0)

class Book(models.Model):
    cover = models.ImageField(u'封面',upload_to='media/book',default='media/book/1.JPG')
    title = models.CharField(u'书名',max_length=50)
    writer = models.CharField(u'作者',max_length=50)
    publish_house = models.CharField(u'出版社',max_length=100)
    publish_date = models.DateTimeField(u'出版日期',default=now, null=True)
    page = models.IntegerField(u'页数')
    price = models.IntegerField(u'定价')
    star = models.FloatField(u'评分',default=5)
    people = models.IntegerField(u'评分人数',default=0)
    summary = models.TextField(u'简介',max_length=500)

class Comment(models.Model):
    name = models.CharField(u'评论人',max_length=50)
    image = models.ImageField(u'头像',default='media/user/1.JPG')
    comment = models.TextField(u'评论',max_length=200)
    book_id = models.IntegerField(u'书的id')
    cover = models.ImageField(u'封面',default='media/book/1.JPG')
    time = models.DateTimeField(u'发布时间',default=now)
    grade = models.IntegerField(u'评分',default=5)

class Mark(models.Model):
    name = models.CharField(u'用户名',max_length=50)
    book_id = models.IntegerField(u'书的id')
    cover = models.ImageField(u'封面', default='media/book/1.JPG')
    change = (
        (0, "想读"),
        (1, "在读"),
        (2, "读过")
    )
    mark = models.IntegerField(u'标记',choices=change)