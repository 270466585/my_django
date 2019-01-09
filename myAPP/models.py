import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 用于保存字符数据的CharField
    pub_date = models.DateTimeField('date published')  # 用于保存时间类型的DateTimeField

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):

    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Usertable(models.Model):
    name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)

