# Backend Assignment Portal

This is a backend system for an assignment submission portal where users can upload assignments, and admins can review and accept or reject them. It uses Flask, MongoDB, and JWT for authentication.

## Features

- **User Endpoints:**

  - `POST /register`: Register a new user.
  - `POST /login`: User login.
  - `POST /upload`: Upload an assignment.
  - `GET /admins`: Fetch all admins.

- **Admin Endpoints:**
  - `POST /register`: Register a new admin.
  - `POST /login`: Admin login.
  - `GET /assignments`: View assignments tagged to the admin.
  - `POST /assignments/:id/accept`: Accept an assignment.
  - `POST /assignments/:id/reject`: Reject an assignment.

## Technologies Used

- **Flask**: Web framework for building the application.
- **MongoDB**: NoSQL database for storing assignments and user data.
- **JWT**: JSON Web Tokens for secure user authentication.
- **Flask-PyMongo**: Flask extension for working with MongoDB.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB
- A text editor or IDE (e.g., VS Code, PyCharm)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/backend-assignment-portal.git](https://github.com/lalitha145/Backend_Challene_GrowthX
   
   ```
