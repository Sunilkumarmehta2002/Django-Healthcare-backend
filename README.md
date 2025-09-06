# 🏥 Healthcare Backend API (Django + DRF)

## 📌 Overview

This is a **robust and secure backend system** for a healthcare application, built using **Django** and **Django REST Framework (DRF)**.

It provides a set of **RESTful APIs** for:

* Managing **patients** and **doctors**
* Handling **user authentication** with JWT
* Creating **patient-doctor mappings**

The backend uses **PostgreSQL** for reliable storage and follows best practices for **scalability and security**.

---

## ✨ Features

* 🔑 **User Authentication** – JWT-based secure login & registration.
* 🧑‍⚕️ **Patient Management** – CRUD operations for patients.
* 👩‍⚕️ **Doctor Management** – CRUD operations for doctors.
* 🔗 **Patient-Doctor Mapping** – Assign doctors to patients (many-to-many).
* 👣 **Database** – PostgreSQL integration.
* 🔐 **Environment Variables** – Configured via `local.env`.

---

## 🛠 Technologies Used

* **Backend Framework**: Django
* **API Framework**: Django REST Framework (DRF)
* **Authentication**: djangorestframework-simplejwt
* **Database**: PostgreSQL
* **Environment Management**: python-decouple

---

## ⚡ Prerequisites

* Python **3.8+**
* PostgreSQL
* Code editor (**VS Code**, **PyCharm**, etc.)
* API client (**Postman**, **Insomnia**)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <repository_url>
cd healthcare-backend
```

### 2️⃣ Set up the Virtual Environment

On **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

On **macOS / Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a file named **`local.env`** in the root directory:

```env
SECRET_KEY=your_super_secret_key_here
DEBUG=True

# PostgreSQL Database Configuration
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server

```bash
python manage.py runserver
```

Your API will now be available at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📡 API Endpoints

All API endpoints are prefixed with `/api/`.

### 🔑 1. Authentication

| Method | Endpoint                   | Description                 |
| ------ | -------------------------- | --------------------------- |
| POST   | `/api/auth/register/`      | Register a new user         |
| POST   | `/api/auth/login/`         | Log in & receive JWT tokens |
| POST   | `/api/auth/token/refresh/` | Refresh JWT access token    |

### 🧑‍⚕️ 2. Patient Management

| Method | Endpoint              | Description                           |
| ------ | --------------------- | ------------------------------------- |
| POST   | `/api/patients/`      | Add a new patient (Auth required)     |
| GET    | `/api/patients/`      | Retrieve all patients (Auth required) |
| GET    | `/api/patients/<id>/` | Get patient details                   |
| PUT    | `/api/patients/<id>/` | Update patient details                |
| DELETE | `/api/patients/<id>/` | Delete a patient                      |

### 👩‍⚕️ 3. Doctor Management

| Method | Endpoint             | Description                      |
| ------ | -------------------- | -------------------------------- |
| POST   | `/api/doctors/`      | Add a new doctor (Auth required) |
| GET    | `/api/doctors/`      | Retrieve all doctors             |
| GET    | `/api/doctors/<id>/` | Get doctor details               |
| PUT    | `/api/doctors/<id>/` | Update doctor details            |
| DELETE | `/api/doctors/<id>/` | Delete a doctor                  |

### 🔗 4. Patient-Doctor Mapping

| Method | Endpoint                              | Description                  |
| ------ | ------------------------------------- | ---------------------------- |
| POST   | `/api/mappings/`                      | Assign a doctor to a patient |
| GET    | `/api/mappings/`                      | Retrieve all mappings        |
| GET    | `/api/mappings/patient/<patient_id>/` | Get doctors for a patient    |
| DELETE | `/api/mappings/<id>/`                 | Remove doctor from patient   |

---

## 🧪 How to Use (with Postman)

1. **Register a User** → `POST /api/auth/register/`
2. **Log in** → `POST /api/auth/login/` → Get `access_token` & `refresh_token`.
3. **Use Authenticated Requests** → Add to headers:

   ```http
   Authorization: Bearer <your_access_token>
   ```
4. **Test Endpoints** → Add patients, doctors, and assign mappings.
5. **Error Handling** → API returns clear error messages and HTTP status codes.

   ---

### 👀 Project Views

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=your-github-username.healthcare-backend)

