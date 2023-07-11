## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Django
  ```sh
  $ pip install django
  
  $ pip install djangorestframework 
  ```

### Installation

Below is an example of how you can install a project

1. Clone the repo
   ```sh
   $ git clone https://github.com/P1ecful/IamCompany
   
   $ cd IamCompany
   ```
2. Make migrations
   ```sh
   $ python manage.py makemigrations
   
   $ python manage.py migrate
   ```
3. Create superuser
   ```sh
   $ python manage.py createsuperuser
   ```
4. Run server
   ```sh
   $ python manage.py runserver
   ```
5. Go to http://127.0.0.1:8000/admin/. Login to the admin panel(data that was entered during registration of the superuser). 
Add Categories and Products, Banners. After, restart the server.
 
