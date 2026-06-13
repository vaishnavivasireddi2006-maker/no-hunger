# Community Food Waste Rescue Network

The **Community Food Waste Rescue Network** is a complete, production-ready web application built in Python Flask, SQLite, and Bootstrap 5. It aligns directly with **UN Sustainable Development Goal 2: Zero Hunger** by creating an efficient circular ecosystem to connect surplus food donors with NGOs and delivery volunteers.

---

## Project Folder Tree

```
csp/
│   app.py                  # Flask Application Routes & Configurations
│   models.py               # Database Schemas & Helpers (SQLAlchemy)
│   init_db.py              # Database Initialization & Seed Script
│   requirements.txt        # Python Packages Dependencies
│   README.md               # User Manual & Credentials
├───static/
│   ├───css/
│   │       style.css       # Custom Sustainability CSS Theme
│   ├───js/
│   │       main.js         # Alerts, Validation, & Freshness Timers
│   │       charts.js       # Chart.js Integration for Admin & Analytics
│   └───uploads/            # Directory for Food Image Uploads
└───templates/
        base.html           # Master Template Layout with Sidebars
        home.html           # Landing Page with Impact Statistics
        about.html          # Mission Details on SDG Goal 2
        contact.html        # Contact Form with Validations
        login.html          # Secure Login Panel
        register.html       # Role-Based Registration Form
        donor_dashboard.html# Donor Portal (Create Donation & Track)
        ngo_dashboard.html  # NGO Portal (Browse surplus, Search, Request)
        volunteer_dashboard.html # Volunteer Portal (Claim, Transport, Complete)
        admin_dashboard.html# Admin Control Panel (Users, Donations, Requests)
        analytics.html      # Public Impact Analytics Dashboard
```

---

## Installation & Setup

Follow these simple steps to run the application locally:

### 1. Prerequisite
Ensure you have **Python 3.8+** installed on your system.

### 2. Install Dependencies
Run the command below in your terminal/command prompt:
```bash
pip install -r requirements.txt
```

### 3. Initialize & Seed Database
This creates the SQLite database `instance/database.db` (or `database.db` depending on your configurations) and populates it with realistic, pre-configured test records:
```bash
python init_db.py
```

### 4. Run Application
Start the development server:
```bash
python app.py
```
Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

---

## Test Accounts & Credentials

To evaluate the application's role-based permissions immediately, use the following pre-seeded credentials:

| Role | Email Address | Password | Description |
|---|---|---|---|
| **Admin** | `admin@foodrescue.org` | `admin123` | Control panel for users, donations, requests & live charts |
| **Donor** | `donor@foodrescue.org` | `password` | Represents "Green Sourdough Bakery" (submit donations) |
| **NGO** | `ngo@foodrescue.org` | `password` | Represents "Hope Food Bank" (browse & request pickup) |
| **Volunteer** | `volunteer@foodrescue.org` | `password` | Represents "Alex Rider" (accept tasks & mark en route/delivered) |

---

## Key Features

1. **Role-Based Access Control (RBAC):** Separate interactive panels for Donors, NGOs, Volunteers, and Admins.
2. **Food Freshness Indicator:** Client-side JavaScript calculates remaining hours/minutes until expiry and marks items dynamically (e.g. *Fresh*, *Expiring Soon*, *Urgent*).
3. **Live Search & Filter:** NGOs can instantly filter through donations by category and search by food name.
4. **Interactive Dashboard Charts:** Integrated Chart.js to show monthly food saving stats, rescue rates, and top donation categories.
5. **Robust Security:** Encrypted password hashing with Werkzeug and secure session-state validation.
