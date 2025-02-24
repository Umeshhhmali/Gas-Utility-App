# Gas Utility Service Request System

## Overview

This is a **Django-based web application** that allows customers to submit and track gas utility service requests. It also provides an **admin panel** where administrators can manage service requests and update their status.

## Features Implemented 

### **Authentication & User Management**

1. **User & Admin Authentication** - Login system for both users and admins.
2. **Profile Management** - Users and admins can view their profile details, including:
   - Profile Picture
   - Name
   - Email
   - Phone Number
   - Address

### **User Functionality**

3. **Service Request Submission** - Users can:
   - Select the type of service request.
   - Provide a description of the issue.
   - Upload a file ( *Currently not working*).
4. **Service Request History** - Users can view previously applied service requests.

### **Admin Functionality**

5. **User Request Management** - Admins can view a list of all service requests submitted by users.
6. **Status Update for Requests** - Admins can update the status of a service request ( *Currently not working*).

---

## Features Not Working 

1. **File Upload in Service Request Form** - Users are currently unable to upload files when submitting a service request.
2. **Status Update in Admin Panel** - Admins cannot update the status of a service request.

---

## Installation & Setup

### **1️⃣  Apply Migrations**

```sh
 python manage.py makemigrations
 python manage.py migrate
```

### **2️⃣ Run the Development Server**

```sh
 python manage.py runserver
```

### **3️⃣ Access the Application**

- **User Login:** `http://127.0.0.1:8000/accounts/login`
- **Admin Panel:** `http://127.0.0.1:8000/accounts/login`

---

## Contact 📬

For any queries, reach out via **[umeshmali341@gmail.com]**.

---
