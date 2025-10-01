# Movies Rating Platform

A full-stack web application that allows users to discover, add, and rate movies. The platform features a Django REST Framework backend and a React frontend.

## Features

*   **User Authentication**: Secure user registration and login using JWT.
*   **Movie Management**: Authenticated users can add new movies to the platform.
*   **Movie Discovery**: Browse and list all movies, with powerful filtering and search capabilities.
*   **Rating System**: Users can rate movies on a scale of 1 to 5 and provide a written review. A user can only rate a movie once, but they can update their existing rating.
*   **Detailed Views**: View detailed information for a specific movie, including its average rating, total number of ratings, and a list of all user reviews.

## API Endpoints

The backend provides the following RESTful API endpoints:

| Method | Endpoint                       | Description                                         | Protected |
| :----- | :----------------------------- | :-------------------------------------------------- | :-------- |
| POST   | `/api/auth/register`           | Register a new user.                                | No        |
| POST   | `/api/auth/login`              | Authenticate a user and receive a JWT.              | No        |
| POST   | `/api/movies`                  | Add a new movie.                                    | Yes       |
| GET    | `/api/movies`                  | List movies with filtering, searching, and pagination. | No        |
| GET    | `/api/movies/{id}`             | Retrieve details for a specific movie.              | No        |
| DELETE | `/api/movies/{id}`             | Delete a movie.                                     | Yes       |
| POST   | `/api/movies/{id}/ratings`     | Add or update a rating for a movie.                 | Yes       |
| GET    | `/api/movies/{id}/ratings`     | List all ratings for a specific movie.              | No        |
| GET    | `/api/users/{id}/ratings`      | List all ratings submitted by a specific user.      | No        |

## Database Schema

The application uses a relational database with the following structure:

*   **User**: `id`, `username`, `email`, `password_hash`, `created_at`
*   **Movie**: `id`, `title`, `genre`, `release_year`, `description`, `created_by`, `created_at`, `ratings_count`, `ratings_avg`
*   **Rating**: `id`, `movie_id`, `user_id`, `rating`, `review`, `created_at`, `updated_at`

## Tech Stack

*   **Backend**: Python, Django, Django REST Framework
*   **Frontend**: React, React Router
*   **Database**: SQLite (development), PostgreSQL (production-ready)

## Setup and Installation

To run this project locally, follow these steps:

### Backend

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

5.  Start the development server:
    ```bash
    python manage.py runserver
    ```
    The backend API will be available at `http://127.0.0.1:8000`.

### Frontend

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2.  Install the required dependencies:
    ```bash
    npm install
    ```

3.  Start the development server:
    ```bash
    npm start
    ```
    The React application will be available at `http://localhost:3000`.

## Running Tests

### Backend

To run the backend tests, navigate to the `backend` directory and run the following command:

```bash
python manage.py test
```

## Design Decisions

### Average Rating Calculation

To optimize performance for listing movies, the `Movie` model includes denormalized fields: `ratings_count` and `ratings_avg`. Instead of calculating the average rating on every movie list request, these fields are updated whenever a rating is created or modified. This approach significantly reduces database load and improves API response times, at the cost of a small overhead on write operations for ratings.

### Authentication

Authentication is handled using JSON Web Tokens (JWT). This method was chosen because it provides a stateless and scalable way to secure the API. Upon successful login, the client receives an access token which is then included in the headers of subsequent requests to protected endpoints.

### Database

SQLite is used as the default database for ease of setup and development. The project is configured to allow a seamless switch to a more robust database like PostgreSQL for production environments. To switch to PostgreSQL, you would need to install the `psycopg2-binary` package and update the `DATABASES` setting in `backend/project/settings.py`.
