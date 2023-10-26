# Generated by Django 4.1.3 on 2023-10-26 21:06


from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showroommodel',
            old_name='discount_for_unique_castomers',
            new_name='discount_for_unique_customers',
        ),
        migrations.AlterField(
            model_name='showroomcardiscount',
            name='name',
            field=models.CharField(max_length=50, verbose_name='discount name'),
        ),
        migrations.AlterField(
            model_name='showroomhistory',
            name='car',
            field=models.CharField(max_length=50, verbose_name='car'),
        ),
        migrations.AlterField(
            model_name='showroomhistory',
            name='customer',
            field=models.CharField(max_length=50, verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='showroommodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name of the showroom'),
        ),
    ]