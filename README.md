# Full Stack Personal Notes Application

This project is a full stack personal notes application built with Flask for the backend and React for the frontend. The application includes user authentication, note creation, and categorization functionalities.

## Features

- User Registration and Login
- Create, View, and Categorize Notes
- User Authentication and Session Management

## Backend Setup

### Prerequisites

- Python 3.x
- MySQL

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/personal_notes_app.git
    cd personal_notes_app/personal_notes_backend
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file with the following content:**

    ```
    SECRET_KEY=your-secret-key
    DATABASE_URL=mysql+mysqlconnector://<username>:<password>@localhost/personal_notes
    ```

5. **Initialize the database:**

    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    python init_db.py
    ```

6. **Run the backend server:**

    ```sh
    flask run
    ```

## Frontend Setup

### Prerequisites

- Node.js
- npm

### Installation

1. **Navigate to the frontend directory:**

    ```sh
    cd ../personal_notes_frontend
    ```

2. **Install the dependencies:**

    ```sh
    npm install
    ```

3. **Start the frontend development server:**

    ```sh
    npm start
    ```


## API Endpoints

### User Authentication

- **Register a new user:**

    `POST /register`

    ```json
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "password123"
    }
    ```

- **Login an existing user:**

    `POST /login`

    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```

- **Logout the current user:**

    `POST /logout`

### Notes Management

- **Get all notes for the logged-in user:**

    `GET /notes`

- **Create a new note:**

    `POST /notes`

    ```json
    {
      "title": "Note Title",
      "description": "Note Description",
      "category": "Note Category"
    }
    ```

### Categories Management

- **Get all categories:**

    `GET /categories`

### User Information

- **Get the logged-in user's information:**

    `GET /user`

## Environment Variables

Create a `.env` file in the backend directory with the following content:


## Running the Application

1. **Backend:**

    ```sh
    cd personal_notes_backend
    flask run
    ```

2. **Frontend:**

    ```sh
    cd ../personal_notes_frontend
    npm start
    ```

## Additional Notes

- Ensure MySQL is running and accessible.
- Replace placeholders like `<username>` and `<password>` with your actual MySQL credentials.
- The backend runs on `http://127.0.0.1:5000` and the frontend on `http://localhost:3000`.
- Make sure CORS is enabled in the backend to allow cross-origin requests from the frontend.


