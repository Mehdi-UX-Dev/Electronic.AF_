# Generated by Django 4.0.4 on 2022-06-05 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('BDK', 'Badakhshan'), ('BDG', 'Badghis'), ('BGH', 'Baghlan'), ('BLK', 'Balkh'), ('BAM', 'Bamyan'), ('DYK', 'Daykundi'), ('FRH', 'Farah'), ('FRB', 'Faryab'), ('GHZ', 'Ghazni'), ('GHR', 'Ghor'), ('HEL', 'Helmand'), ('HRT', 'Herat'), ('JZJ', 'Jowzjan'), ('KBL', 'Kabul'), ('KDR', 'Kandahar'), ('KPS', 'Kapisa'), ('KST', 'Khost'), ('KNR', 'Kunar'), ('KDZ', 'Kunduz'), ('LGH', 'Laghman'), ('LGR', 'Logar'), ('NGR', 'Nangarhar'), ('NMZ', 'Nimruz'), ('NRT', 'Nuristan'), ('ORZ', 'Oruzgan'), ('PTI', 'Paktia'), ('PTK', 'Paktika'), ('PJR', 'Panjshir'), ('PAR', 'Parwan'), ('SMN', 'Samangan'), ('SRP', 'Sar-e-Pol'), ('TKH', 'Takhar'), ('WDK', 'Wardak'), ('ZBL', 'Zabul')], max_length=3)),
                ('district', models.CharField(max_length=55)),
                ('home_address', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(blank=True, max_length=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product name')),
                ('category', models.CharField(choices=[('LT', 'Laptop'), ('DT', 'Desktop')], max_length=2)),
                ('cpu', models.CharField(max_length=255)),
                ('gpu', models.CharField(max_length=255)),
                ('memory', models.CharField(choices=[('4', '4GB'), ('8', '8GB'), ('16', '16GB'), ('32', '32GB'), ('64', '64GB'), ('128', '128GB')], max_length=3)),
                ('storage', models.CharField(choices=[('256', '256GB'), ('512', '512GB'), ('1000', '1TB'), ('2000', '2TB'), ('4000', '4TB')], max_length=4)),
                ('storage_type', models.CharField(choices=[('1', 'HDD'), ('2', 'SSD')], max_length=1)),
                ('os', models.CharField(blank=True, max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('OD', 'OutForDelivery'), ('D', 'Delivered')], max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.address')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('thumbnail', models.ImageField(blank=True, upload_to='products/tumbnails')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
