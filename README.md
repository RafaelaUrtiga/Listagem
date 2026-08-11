# Listagem

**Attendance & registration management system** built with **Python + Django** — client registry with check-in verification, photo records and soft-delete archiving, following Django's **MVT architecture**.

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)

## Overview

Listagem is a **full-stack web application** for managing member registration and attendance verification — a workflow used by schools, NGOs and community programs. Built with **Django 5** on its **MVT (Model-View-Template) architecture**, the system is organized into two dedicated apps: `cadastro` (member registry) and `listagem` (attendance listing & check-in).

## Key Features

- **Member registry (CRUD)** with personal data, address, membership card number and **photo upload**
- **UUID primary keys** — non-sequential, secure record identifiers
- **Soft-delete / archiving pattern**: records are archived with timestamp and author instead of destroyed, preserving data history
- **Automatic audit fields**: `created_at` / `updated_at` tracked by the ORM
- **Attendance listing & registration check** via the `listagem` app
- **Modular architecture**: independent Django apps with clear separation of concerns
- **Django ORM** with migrations for versioned database schema

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | Django 5.2 (MVT) |
| Database | SQLite + Django ORM |
| Data Modeling | UUID keys, ImageField, soft-delete pattern |

## Getting Started

```bash
# 1. Clone and set up a virtual environment
git clone https://github.com/RafaelaUrtiga/Listagem.git
cd Listagem
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Prepare the database and run
python manage.py migrate
python manage.py runserver
```

The app is then available at `http://localhost:8000`.

## Project Structure

```
├── cadastro/          # Member registry app (models, views, templates)
├── listagem/          # Attendance listing & check-in app
├── manage.py          # Django management CLI
└── requirements.txt   # Python dependencies
```

## Skills Demonstrated

**Python** · **Django** · **MVT architecture** · **ORM & data modeling** · **relational databases (SQL)** · **CRUD applications** · **soft-delete patterns** · **database migrations** · **backend development**

---

📫 Feedback and contributions are welcome — feel free to open an issue.
