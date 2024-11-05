# Generated by Django 5.1.3 on 2024-11-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0004_auto_20220211_0716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalexpense',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Gasto', 'verbose_name_plural': 'historical Gastos'},
        ),
        migrations.AlterModelOptions(
            name='historicalexpensecategory',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Categoria de Gasto', 'verbose_name_plural': 'historical Categorias de Gastos'},
        ),
        migrations.AlterModelOptions(
            name='historicalmerma',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Merma', 'verbose_name_plural': 'historical Mermas'},
        ),
        migrations.AlterModelOptions(
            name='historicalpaymenttype',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Medio de Pago', 'verbose_name_plural': 'historical Medio de Pagos'},
        ),
        migrations.AlterModelOptions(
            name='historicalsupplier',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Proveedor', 'verbose_name_plural': 'historical Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='historicalvoucher',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Comprobante', 'verbose_name_plural': 'historical Comprobantes'},
        ),
        migrations.AlterField(
            model_name='historicalexpense',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalexpensecategory',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalmerma',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpaymenttype',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalsupplier',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalvoucher',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
