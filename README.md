# TropicalStudio-ManagementSystem

# Description
- TropicalStudio allows the user to schedule an appointment with a beauty parlor for a specific date and time.
- It allows customers to schedule appointments online from any place just with a few clicks. This project also aids in management tasks like creating, updating, deleting services and employees.

# Tools
- Python version -3.11 Version
- Programming Language Used -	Python Django Language
- IDE Tool - PyCharm
- Database - SQLite
- Frontend - Bootstrap5, HTML, CSS, JavaScript


# User Features - normal user
- Sign up - the user need to make an account and to login into it to be able to make an appointment
- Login and Logout - he can login and logout 
- Change password - the user can change his password
- Make an appointment flux - the user will select the service and after that he can choose the date and time of his appointment. He will receive a confirmation message if the appointment it's registered. The user can see the history of his appointments in his account.

# User Features - user with permissions in Django admin
- In Django admin I created a group named 'STAFF'. The admin can add users in this group and all of them have extra permissions
- In navbar they will see another 2 sections 'Servicii'(Services) and 'Angajati'(Employees). They can apply CRUD method which means they can create, delete, update and view the details. Also, they can see the list of services and employees.

# Future implementation
- after booking an appointment the user will receive a confirmation e-mail with all details



