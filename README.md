# Django Project

This is a Django web application. Follow the instructions below to set up and run the project and again welcome to Django.

---

## How to Run This Django Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

# Django Field Types: String vs Slug

## What is Django?
Django is a high-level Python web framework that helps you build secure, scalable web applications quickly.

---

## What is a Model Field?
A model field in Django defines the type of data that can be stored in a database column for a model.

---

## What is a String Field?
**String fields** in Django are used to store text data.

- **CharField**: For short strings (like names, titles).
- **TextField**: For longer text (like descriptions, content).

**Example:**
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```
- You can store any characters, spaces, and symbols.

---

## What is a Slug Field?
A **SlugField** is a special string field for storing URL-friendly text.

- Only letters, numbers, hyphens (`-`), and underscores (`_`) are allowed.
- Used for creating readable URLs.

**Example:**
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
```
- Valid slug: `my-article-title`
- Invalid slug: `my article!` (contains space and special character)

---

## Why Use Slugs?
- **SEO-friendly URLs**: `/blog/my-django-tutorial/`
- **Human-readable**: Easy to understand and share
- **Consistent**: URLs don’t break if the title changes

---

## How to Auto-Generate a Slug?
You can use Django’s `slugify` utility to create slugs from titles.

**Example:**
```python
from django.utils.text import slugify

title = "My Amazing Django Tutorial!"
slug = slugify(title)  # Result: "my-amazing-django-tutorial"
```

**In a model:**
```python
def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super().save(*args, **kwargs)
```

---

## How to Use Slugs in URLs?
**Example:**
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
```
This lets you access articles by their slug in the URL.

---

## Key Differences Table

| Feature           | String Field        | Slug Field                |
|-------------------|--------------------|---------------------------|
| Allowed Characters| All                | Letters, numbers, `-`, `_`|
| Spaces            | Yes                | No                        |
| Special Characters| Yes                | No                        |
| URL-safe          | No                 | Yes                       |

---

## Summary
- Use **CharField/TextField** for general text.
- Use **SlugField** for URL-friendly identifiers.
- Slugs make your URLs readable and good for SEO.
- Auto-generate slugs using `slugify`.

---

## Example Data

- String: `"My Article Title!"`
- Slug: `"my-article-title"`

---

## What is `__pycache__`?
- `__pycache__` is a folder where Python stores compiled bytecode files (`.pyc`) for faster execution.
- You should **not** add `__pycache__` to your git repository.

---

## Best Practices
- Use string fields for display.
- Use slug fields for URLs.
- Add `__pycache__/` to `.gitignore`.

---

## Learning Recap
- Django basics: models, fields, URLs
- Difference between string and slug fields
- How to use slugs for SEO and readable URLs
- How Python optimizes code with `__pycache__`

## More coming soon......