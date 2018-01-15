from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField('姓名', max_length=64)
    age = models.SmallIntegerField('年龄')
    # bpub_date = models.DateTimeField()
    email = models.EmailField(blank=True)
    choices = (
        (1, '男'),
        (2, '女'),
        (3, '未知')
    )
    sex = models.SmallIntegerField('性别', choices=choices)

    class Meta:
        verbose_name = '用户列表'
        verbose_name_plural = '用户列表'

    def __str__(self):
        str = '%s         %s' % (self.name, self.email)
        return str

