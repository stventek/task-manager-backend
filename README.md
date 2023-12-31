# task-manager-backend

Task manager REST API made using Django REST Framework.

## Features

- CRUD Sections and Tasks, such operations are restricted to the user who created them.
- User Authentication.

## Technical Features

- **Swagger Documentation** Access comprehensive API documentation through Swagger.
- **Filtering:** filter tasks and sections based on the desired criteria.
- **Paginated response:** Manage the response efficiently with paginated responses.
- **Sorting:** Sort tasks and sections based on the desired criteria.
- **Permissions and Groups** fine-grained control over user access with permissions and user groups.
- **JWT and sessions:** Ensure secure authentication using JSON Web Tokens (JWT) or sessions.

## Swagger documentation

- Read the documentation with redoc at: http://localhost:8000/api/schema/redoc/
- Readt the documentation with swagger ui at: http://localhost:8000/api/schema/swagger-ui/

## Installation and Setup

1. Clone the repository:

```
git clone <repository_url>
```

2. Create a virtual environment and activate it:

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Configure the project settings:

- Rename the `.env.example` file to `.env` and update the settings accordingly.

5. Apply database migrations:

```
python manage.py migrate
```

6. Start the development server:

```
python manage.py runserver
```

## Endpoints

Brief description about the endpoints

- **/admin/:** Django admin interface.
- **/api-auth/:** REST Framework Authentication to use browseable API.
- **GET, POST, PATCH, DELETE /api/section/:** Section CRUD
- **GET, POST, PATCH, DELETE /api/task/:** Task CRUD
- **POST /api/token/:** Obtain JWT Token
- **POST /api/token/refresh/:** Refresh JWT Token
- **POST /api/token/verify/:** Verify JWT Token

## License

This project is licensed under the [MIT License](LICENSE).
