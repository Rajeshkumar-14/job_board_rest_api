from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import JobBoard
from .serializers import JobBoardSerializer
from board_manager.serializers import UserSerializer
from faker import Faker

class AuthViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()

    def create_fake_user_data(self):
        return {
            "username": self.fake.user_name(),
            "password": self.fake.password(),
            "email": self.fake.email(),
        }

    def test_signup(self):
        data = self.create_fake_user_data()
        response = self.client.post("/auth/sign-up", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com"
        )
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post("/auth/login", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)


    def test_security_checks_unauthenticated(self):
        # unauthorized access to the signup and login views
        response = self.client.get("/auth/sign-up")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.get("/auth/login")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class JobViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.fake = Faker()
    def create_fake_job_listing_data(self):
        return {
            "job_title": self.fake.job(),
            "job_description": self.fake.text(),
            "requirements": self.fake.words(3),
            "location": self.fake.city(),
            "salary": self.fake.random_element(elements=["$80,000 - $100,000", "$70,000 - $90,000"]),
            "company_name": self.fake.company(),
        }

    def test_create_job_listing(self):
        data = self.create_fake_job_listing_data()
        data["requirements"] = "Valid requirements data"
        response = self.client.post("/api/job-listings/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobBoard.objects.count(), 1)


    def test_get_job_details(self):
        job_listing = JobBoard.objects.create(**self.create_fake_job_listing_data())
        response = self.client.get(f"/api/job-listings/{job_listing.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["job_title"], job_listing.job_title)

    def test_search_jobs(self):
        job1 = JobBoard.objects.create(**self.create_fake_job_listing_data())
        job2 = JobBoard.objects.create(**self.create_fake_job_listing_data())

        # Search for jobs by location
        response = self.client.get(f"/api/job-listings/?search={job1.location}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Search for jobs by job title
        response = self.client.get(f"/api/job-listings/?search={job2.job_title}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
