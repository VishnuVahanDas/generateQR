# QR Code Generator

This Django project provides a simple interface to generate a QR code for any URL and store it in the database.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations:
   ```bash
   python manage.py migrate
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Visit `http://localhost:8000/` to generate a QR code.

Generated images are stored in the `media/qr_codes/` directory.
