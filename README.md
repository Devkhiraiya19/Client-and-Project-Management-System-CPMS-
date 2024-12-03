Client and Project Management System (CPMS)
Overview
The Client and Project Management System (CPMS) is a robust backend application built using Django REST Framework with MySQL/Postgres as the database. It provides a structured approach to manage users, clients, and projects efficiently. The system supports CRUD operations for clients and projects, user assignment to projects, and retrieval of project details specific to logged-in users.
Features
Client Management

Register new clients.
Fetch client details, including their assigned projects.
Edit or delete client information.
Project Management

Add new projects under specific clients.
Assign multiple users to a project.
Retrieve all projects assigned to logged-in users.
User Integration

Uses Django's built-in user management system for user authentication and authorization.


Endpoints
Clients
GET /clients/: List all clients.
POST /clients/: Create a new client.
GET /clients/:id: Retrieve a client and their associated projects.
PUT /PATCH /clients/:id: Update client information.
DELETE /clients/:id: Delete a client.
Projects
POST /projects/: Create a new project under a client and assign users.
GET /projects/: List all projects assigned to the logged-in user.

Technology Stack
Backend Framework: Django REST Framework
Database: MySQL
Authentication: Django's default authentication system



