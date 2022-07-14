from django.db import models

# Create your models here.
class DB_tool(models.Model):
    name = models.CharField(max_length=30,default='')
    stime =  models.CharField(max_length=30,default='')
    def __str__(self):
        return self.name


class DB_order(models.Model):
    name =  models.CharField(max_length=30,default='') #工单标题
    body =  models.CharField(max_length=1000,default='') #工单内容
    uid_from =  models.CharField(max_length=30,default='') #提交人id
    ctime =  models.CharField(max_length=30,default='') #创建时间
    state = models.BooleanField(default=False) #状态，默认假，即未完成
    def __str__(self):
        return self.name