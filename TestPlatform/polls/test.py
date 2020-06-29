#python manage.py shell
from polls.models import Choice, Question
from django.utils import timezone
insert = Question(question_text="python-django3.0",pub_date=timezone.now())
insert.save()
# insert.id
insert.question_text #查询question_text字段值
# insert.question_text = "django" 修改实例，修改好要进行保存
insert.pub_date #查询pub_date字段值
# Question.objects.all() 查询所有数据
