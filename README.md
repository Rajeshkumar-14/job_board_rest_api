# Job Board Backend

Job Board Backend is a Django Rest Framework (DRF) application for managing job postings and applications. It provides a secure API with token-based authentication for posting job vacancies and enabling user applications.

## Technologies Used

- Python
- Django
- Django Rest Framework (DRF)
- Poetry
- Django Filters

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rajeshkumar-14/job_board_rest_api.git
   ```
2. **Create and Activate Conda Environment:**

   - Create a new Conda environment or use your existing environment:

     ```bash
     conda create --name job-board-env
     ```

   - Activate the Conda environment:

     ```bash
     conda activate job-board-env
     ```
3. **Install Dependencies:**

   - Install Poetry:

     ```bash
     pip install poetry
     ```

   - Run this command after installing Poetry:

     ```bash
     poetry install
     ```

4. **Database Setup:**

   - Run these commands to migrate models:

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

   - If the above commands don't work, try:

     ```bash
     python manage.py makemigrations authentication
     python manage.py makemigrations job_board
     python manage.py migrate
     ```
5. **Create Superuser:**

   ```bash
   python manage.py createsuperuser
    ```
6. **Run Server**
  ```bash
    python manage.py runserver
  ```
## Usage

- Access the API documentation at [http://localhost:8000/swagger/](http://localhost:8000/swagger/) or [http://localhost:8000/redoc/](http://localhost:8000/redoc/) after starting the development server.

### Accessing Endpoints with Postman

1. **POST New User (Signup):**
   - Method: POST
   - URL: [http://localhost:8000/auth/sign-up/](http://localhost:8000/auth/sign-up/)
   - Body (JSON):
     ```json
     {
         "username": "user",
         "password": "password"
     }
     ```
   - Response (JSON):
     ```json
     {
         "message": "User created successfully"
     }
     ```

2. **User Login:**
   - Method: POST
   - URL: [http://localhost:8000/auth/login/](http://localhost:8000/auth/login/)
   - Body (JSON):
     ```json
     {
         "username": "user",
         "password": "password"
     }
     ```
   - Response (JSON):
     ```json
     {
         "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
     }
     ```
   ⚠️ **Note:** Paste the token in the header with `Key` as `Authorization` and `value` as `Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...` to access the api.

3. **GET All Job Listings:**
   - Method: GET
   - URL: [http://localhost:8000/api/job-listings/](http://localhost:8000/api/job-listings/)
   - Response: 200 OK

4. **POST a New Job Listing:**
   - Method: POST
   - URL: [http://localhost:8000/api/job-listings/](http://localhost:8000/api/job-listings/)
   - Body (JSON): JSON data representing the new job listing
   - Response: 201 Created


5. **PUT Update a Job Listing:**
   - Method: PUT
   - URL: [http://localhost:8000/api/job-listings/<id>/](http://localhost:8000/api/job-listings/<id>/)
   - Body (JSON): JSON data with updated job listing details
   - Response: 200 OK

6. **DELETE a Job Listing:**
   - Method: DELETE
   - URL: [http://localhost:8000/api/job-listings/<id>/](http://localhost:8000/api/job-listings/<id>/)
   - Response: 204 No Content


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.