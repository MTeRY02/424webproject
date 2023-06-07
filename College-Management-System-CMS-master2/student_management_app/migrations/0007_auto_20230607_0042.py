
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_auto_20210528_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='doctor',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='student_num',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
