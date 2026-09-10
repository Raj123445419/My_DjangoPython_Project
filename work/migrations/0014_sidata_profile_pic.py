from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_orderreturnrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidata',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
