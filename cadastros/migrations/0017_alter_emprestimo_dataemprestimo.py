# Generated by Django 3.2.9 on 2022-06-10 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_auto_20220609_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='dataEmprestimo',
            field=models.DateField(auto_now=True, help_text='Informe a data de empréstimo do livro', verbose_name='Data do Empréstimo'),
        ),
    ]