# Employee Management System

A Django-based Employee Management System for managing employee records, attendance, and more.

## Deployment on Render

### Prerequisites
- GitHub account
- Render.com account
- Python 3.10+

### Deployment Steps

1. **Prepare your repository**
   - Push your code to a GitHub repository

2. **Create a new Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

3. **Configure the Web Service**
   - **Name**: Choose a name for your service (will be part of the URL)
   - **Region**: Choose the closest region
   - **Branch**: main or master (depending on your repository)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn empmanagement.wsgi`

4. **Environment Variables**
   Add these environment variables in the Render dashboard:
   ```
   PYTHON_VERSION=3.10.0
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=*
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

6. **After Deployment**
   - Run migrations: Go to the "Shell" tab in Render and run:
     ```
     python manage.py migrate
     python manage.py createsuperuser
     ```

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Features
- Employee management
- Attendance tracking
- Department management
- User authentication and authorization
