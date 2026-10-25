# Library API

A Django REST Framework API for managing books. Each book has a title, author, ISBN, and creation timestamp. ISBN values are normalized and validated, and duplicate ISBNs are rejected.

## Requirements

- Python
- Git (optional, for cloning or contributing)

## Setup on Windows

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Set a secret key for the current PowerShell session:

```powershell
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

This generates a new key for the current session. Set your own key persistently if needed, and never commit it to the repository.

Apply migrations and start the development server:

```powershell
python manage.py migrate
python manage.py runserver
```

The API root is `http://127.0.0.1:8000/api/`, and the book endpoints are at `http://127.0.0.1:8000/api/books/`. The Django admin is at `http://127.0.0.1:8000/admin/`.

To create an administrator account:

```powershell
python manage.py createsuperuser
```
