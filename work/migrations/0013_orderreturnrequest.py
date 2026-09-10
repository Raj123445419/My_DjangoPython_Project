import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_userorder_orderitem_readinghistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='payment_method',
            field=models.CharField(default='Cash on Delivery (COD)', max_length=60),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='status',
            field=models.CharField(
                choices=[
                    ('Placed', 'Order Placed'),
                    ('Processing', 'Processing'),
                    ('Out for Delivery', 'Out for Delivery'),
                    ('Delivered', 'Delivered'),
                    ('Cancelled', 'Cancelled'),
                    ('Return Requested', 'Return Requested'),
                    ('Replacement Requested', 'Replacement Requested'),
                    ('Return Approved', 'Return Approved'),
                    ('Replacement Approved', 'Replacement Approved'),
                    ('Returned & Refunded', 'Returned & Refunded'),
                    ('Replacement Dispatched', 'Replacement Dispatched'),
                ],
                default='Placed',
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name='OrderReturnRequest',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'request_type',
                    models.CharField(
                        choices=[
                            ('Return', 'Return (Refund)'),
                            ('Replacement', 'Replacement (Exchange)'),
                        ],
                        default='Return',
                        max_length=30,
                    ),
                ),
                (
                    'reason',
                    models.CharField(
                        choices=[
                            ('Damaged Product / Pages Torn', 'Damaged Product / Pages Torn'),
                            ('Defective Printing / Missing Pages', 'Defective Printing / Missing Pages'),
                            ('Wrong Manga Volume Delivered', 'Wrong Manga Volume Delivered'),
                            ('Language / Edition Mismatch', 'Language / Edition Mismatch'),
                            ('Other Issue', 'Other Issue'),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    'is_damaged',
                    models.BooleanField(
                        default=False,
                        help_text='True if item arrived damaged',
                    ),
                ),
                (
                    'description',
                    models.TextField(
                        help_text="Detailed explanation from customer"
                    ),
                ),
                (
                    'refund_payment_method',
                    models.CharField(
                        default='Cash on Pickup',
                        help_text='Cash on Pickup / UPI / Bank Transfer',
                        max_length=60,
                    ),
                ),
                (
                    'refund_details',
                    models.CharField(
                        blank=True,
                        help_text='UPI ID or Phone or Account Number for refund',
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    'damage_image',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to='return_proofs/',
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('Pending Verification', 'Pending Verification'),
                            ('Approved for Return & Refund', 'Approved for Return & Refund'),
                            ('Approved for Replacement', 'Approved for Replacement'),
                            ('Replacement Dispatched', 'Replacement Dispatched'),
                            ('Rejected - Damage Required for Return', 'Rejected - Damage Required for Return (Replacement Eligible)'),
                            ('Rejected', 'Rejected'),
                            ('Completed', 'Completed'),
                        ],
                        default='Pending Verification',
                        max_length=70,
                    ),
                ),
                (
                    'admin_reply',
                    models.TextField(
                        blank=True,
                        help_text='Admin verification decision and reply message to customer',
                        null=True,
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'order',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='return_request',
                        to='work.userorder',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='work.sidata',
                    ),
                ),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
