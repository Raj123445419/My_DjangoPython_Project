import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywork.settings')
django.setup()

from django.core.management import call_command

print("Running migrate...")
call_command('migrate')
print("Migration completed successfully!")
