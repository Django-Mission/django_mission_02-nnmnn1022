# Generated by Django 4.0.3 on 2022-04-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0007_remove_inquiry_image_title_inquiry_phone_checkbox_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='email_checkbox',
            field=models.BooleanField(default=True, verbose_name='e-mail로 답변을 받겠습니다.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_checkbox',
            field=models.BooleanField(default=False, verbose_name='문자메시지로 답변을 받겠습니다.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_number',
            field=models.IntegerField(verbose_name='전화번호'),
        ),
    ]
