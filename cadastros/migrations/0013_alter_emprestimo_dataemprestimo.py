# Generated by Django 3.2.9 on 2022-05-22 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0012_alter_emprestimo_dataemprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='dataEmprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 19, 40, 54, 130588), help_text='Informe a data de empréstimo do livro', verbose_name='Data do Empréstimo'),
        ),
    ]
