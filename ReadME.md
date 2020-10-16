## Steps To Creating models 

1. Define your database layout in <app_name>/models.py
2. Activating models by adding "<app_name>.apps.ClassName" in <site_name>/settings.py¶
3. run the below command 
```bash
    python manage.py makemigrations <app_name>

    python manage.py sqlmigrate <app_name> 0001

    python manage.py migrate

    # to interactive with model
    python manage.py shell

```

### Creating an admin user

```bash
    python manage.py createsuperuser
```