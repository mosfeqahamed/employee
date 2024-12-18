
![Alt text](./dashboard.png)

# Django Records Management System

This is a simple Django web application for managing employee records. It includes features like searching, sorting, filtering, pagination, and CRUD operations (Create, Read, Update, Delete) for records. The system also handles image uploads with resizing functionality to optimize loading times.

## Features

- **Search & Filter**: Search records by name, email, date of birth, and mobile number.
- **Sort**: Sort records by full name, email, mobile, and date of birth in ascending or descending order.
- **Pagination**: Navigate through records with pagination controls.
- **CRUD Operations**:
  - Create new records with photo upload.
  - Update existing records.
  - Delete records with confirmation.
- **Image Upload**: Uploaded photos are resized to a maximum of 300x300 pixels to improve performance.
  
## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 4
- **Database**: SQLite (default)
- **Image Processing**: Pillow (PIL)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd employee
   
2. cd env/Scripts

Activate the activate.bat: .\activate.bat

3. comming back to employee directory and write " cd employ_management " to the terminal

4.Install dependencies:
pip install -r requirements.txt

5.Set up the database:
python manage.py migrate

6.Create a superuser to access the admin panel:
python manage.py createsuperuser

7.Run the development server:
python manage.py runserver

8.Access the application at http://127.0.0.1:8000/.
