## Task Overview

A tech startup is building a user registration system where each user must have a unique email address. Currently, the API allows multiple registrations with the same email, leading to confusion and operational issues. The business needs a reliable way to prevent duplicate user accounts and provide clear feedback to users attempting to register with an already-used email.

## Guidance

You are implementing a backend API for user registration using FastAPI and PostgreSQL. The system must guarantee that no two users can register with the same email address. This requires a combination of proper database schema design, API-level validation, and robust error handling. Organize your code using routers, services, and models for maintainability. Follow best practices for async database operations and containerization. Ensure all environment variables are managed securely and the API is properly documented with OpenAPI.

## Objectives

- Implement a POST endpoint for user registration that receives email and password, creates a user, and returns their details.
- Ensure the email address is unique both at the database level and within the API logic.
- Return a clear error message and appropriate status code if a duplicate email registration is attempted.
- Structure your project into routers, services, models, and database modules, adhering to best practices for FastAPI and SQLAlchemy async usage.
- Containerize the application using Docker and Docker Compose, with PostgreSQL as the backing database.
- Use environment variables for configuration, and provide OpenAPI documentation for your endpoints.

## How to Verify

- Register a new user with a unique email and confirm the API returns a successful response with user details.
- Attempt to register another user with the same email and verify that the API responds with a client error and an informative message about email duplication.
- Check the PostgreSQL database to ensure only one user record exists for each unique email address.
- Review the OpenAPI documentation and ensure the registration endpoint is present and well-described.
- Ensure the application runs successfully with Docker Compose and all environment variables are configurable.
