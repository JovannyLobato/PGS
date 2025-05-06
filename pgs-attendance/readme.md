#  PGS Attendance System

Este proyecto es un sistema de asistencia desarrollado en Python, utilizando FastAPI, PyQt5 y PostgreSQL.

---

##  Estructura del Proyecto

.
├── config
│   └── database.py
├── controllers
│   └── registro_controller.py
├── dao
│   ├── kid_dao.py
│   ├── parent_dao.py
│   ├── registro_dao.py
│   └── teacher_dao.py
├── init_db.py
├── main.py
├── models
│   ├── __init__.py
│   ├── kid.py
│   ├── parent.py
│   ├── registro.py
│   └── teacher.py
├── readme.md
├── requirements.txt
├── run.sh
├── utils
│   └── fingerprint_utils.py
└── views
    └── main_window.py



---

##  Requisitos

- Python 3.10 o superior
- pip
- Git (opcional)
- PostgreSQL 

---

##  Instalación y Ejecución

1. Abre una terminal en el directorio del proyecto.
2. Ejecuta el script `run.sh`:

```bash
./run.sh

