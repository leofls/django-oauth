Istale o Django OAuth Toolkit:
pip install django-oauth-toolkit

adicione em settings:
```py
INSTALLED_APPS = [
    ...
    'oauth2_provider',
]
```

Faça o migrate:
```sh
python manage.py migrate 
```

Crie sua conta 
```
python manage.py migrate
```

Após instalar vá para o admin e faça login 
``` 
http://127.0.0.1:8000/admin/ 
```
Crie uma nova aplicação em:
``` 
http://127.0.0.1:8000/o/applications/register/ 
``` 
Preencha os campos 
