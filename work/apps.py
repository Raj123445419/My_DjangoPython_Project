from django.apps import AppConfig
from django.db import connection


class WorkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'work'

    def ready(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA table_info(work_sidata);")
                columns = [row[1] for row in cursor.fetchall()]
                if columns and 'profile_pic' not in columns:
                    cursor.execute("ALTER TABLE work_sidata ADD COLUMN profile_pic varchar(100) NULL;")
        except Exception:
            pass

