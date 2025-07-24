# Developer Setup Guide - project-build-a-modern

This guide outlines the setup process for developers working on `project-build-a-modern`, a modern e-commerce platform.  We recommend using Docker for development, but native setup instructions are also provided.

## Prerequisites

### Required Software Versions

* **Docker:**  Version 20.10.0 or higher (for Docker option)
* **Docker Compose:** Version 1.29.0 or higher (for Docker option)
* **Node.js:** Version 16 or higher (for both options)
* **npm (or yarn):**  The Node.js package manager (for both options)
* **Python:** Version 3.9 or higher (for native backend setup)
* **PostgreSQL:** Version 13 or higher (or compatible version specified in `docker-compose.yml` if using Docker)


### Development Tools

* Git
* Text editor or IDE (VS Code recommended)

### IDE Recommendations and Configurations

* **VS Code:**  Highly recommended. Install extensions for:
    * Python (Pylance, Python extension for VS Code)
    * JavaScript/TypeScript (TypeScript and ESLint)
    * Docker
    * PostgreSQL


## Local Development Setup

### Option 1: Docker Development (Recommended)

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-build-a-modern
   ```

2. **Docker Setup:** Ensure Docker and Docker Compose are installed and running.

3. **Development `docker-compose.yml` Configuration:**  The project should include a `docker-compose.yml` file defining the services (e.g., frontend, backend, database).  This file manages containers for each service.  Example:

   ```yaml
   version: "3.9"
   services:
     web:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - api
     api:
       build: ./backend
       ports:
         - "8000:8000"
       environment:
         - DATABASE_URL=postgresql://postgres:password@db:5432/ecommerce_db
     db:
       image: postgres:13
       environment:
         - POSTGRES_USER=postgres
         - POSTGRES_PASSWORD=password
         - POSTGRES_DB=ecommerce_db
   ```

4. **Hot Reload Setup:**  The frontend build process (e.g., using `webpack` or `vite`) should include hot reloading for faster development.  This is typically configured within the `frontend` directory's build tools.


### Option 2: Native Development

1. **Backend Setup:**
   * Create a Python virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * Install backend dependencies:
     ```bash
     pip install -r requirements.txt
     ```
2. **Frontend Setup:**
   * Install Node.js and npm (or yarn).
   * Navigate to the frontend directory: `cd frontend`
   * Install frontend dependencies:
     ```bash
     npm install
     ```
3. **Database Setup:**
   * Install PostgreSQL.
   * Create a database named `ecommerce_db` (or as specified in your database configuration).
   * Configure database credentials in your backend settings.


## Environment Configuration

### Required Environment Variables

The `.env` file (or equivalent) should contain:

* `DATABASE_URL`:  The connection string for your database.
* `STRIPE_SECRET_KEY`: Your Stripe secret key for payment processing.
* `STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable key.
* `EMAIL_HOST`: Your email server host.
* `EMAIL_PORT`: Your email server port.
* `EMAIL_USERNAME`: Your email username.
* `EMAIL_PASSWORD`: Your email password.
* `SECRET_KEY` (for backend security)

### Local Development `.env` File Setup

Create a `.env` file in the root directory (or as specified in your project) and populate it with your development environment variables.  **Never commit your `.env` file to version control.**

### Configuration for Different Environments

Use environment variables to configure settings for different environments (development, staging, production).  This could involve using a `.env.development`, `.env.staging`, and `.env.production` file, or a more sophisticated configuration management system.


## Running the Application

### Start Commands for Development

* **Docker:** `docker-compose up -d`
* **Native:**  Start the backend server (e.g., `python manage.py runserver`) and then the frontend development server (e.g., `npm start`).

### How to Access Frontend and Backend

* **Frontend:** Access the e-commerce platform at `http://localhost:3000` (or the port specified in your `docker-compose.yml` or frontend configuration).
* **Backend API:** Access the backend API at `http://localhost:8000/api/` (or the port specified in your `docker-compose.yml` or backend configuration).

### API Documentation Access

Swagger or similar API documentation tools should be integrated to provide documentation for the backend API endpoints.


## Development Workflow

### Git Workflow and Branching Strategy

Use Git for version control.  A common strategy is Gitflow (feature branches for new features, develop branch for integration, master branch for production).

### Code Formatting and Linting Setup

Use linters (e.g., `flake8` for Python, `ESLint` for JavaScript) and code formatters (e.g., `black` for Python, `Prettier` for JavaScript) to ensure consistent code style.

### Testing Procedures

Implement unit tests, integration tests, and end-to-end tests.  Use a testing framework (e.g., `pytest` for Python, `Jest` for JavaScript).

### Debugging Setup

Use your IDE's debugging tools or command-line debuggers (e.g., `pdb` for Python, Node.js debugger).


## Database Management

### Running Migrations

Use database migration tools (e.g., Alembic for Python, Sequelize migrations for Node.js) to manage database schema changes.

### Seeding Development Data

Create scripts to seed your database with sample data for development purposes.

### Database Reset Procedures

Implement a procedure to easily reset your development database to a clean state.


## Testing

### Running Unit Tests

Run unit tests using your chosen testing framework (e.g., `pytest` or `Jest`).

### Running Integration Tests

Run integration tests to test the interaction between different components of your application.

### Test Coverage Reports

Generate test coverage reports to track the percentage of your code covered by tests.


## Common Development Tasks

### Adding New API Endpoints

1. Define the API endpoint in the backend.
2. Implement the logic for the endpoint.
3. Write unit and integration tests.
4. Update API documentation.

### Adding New Frontend Components

1. Create the component in the frontend.
2. Integrate the component into the application.
3. Write unit tests.

### Database Schema Changes

1. Create a database migration.
2. Update the models.
3. Update the related API endpoints and frontend components.

### Adding Dependencies

Add dependencies using `pip` (for Python) and `npm` or `yarn` (for JavaScript).  Update your project's dependency files accordingly.


## Troubleshooting

### Common Setup Issues

* Check that all prerequisites are installed correctly.
* Verify that environment variables are set properly.
* Check the logs for error messages.

### Port Conflicts Resolution

If a port is already in use, change the port number in your configuration files.

### Dependency Issues

Ensure all dependencies are compatible.  Use a virtual environment for Python to isolate dependencies.

### Environment Variable Problems

Double-check your `.env` file and ensure that environment variables are correctly loaded.


## Contributing

### Code Style Guidelines

Follow the project's code style guidelines (e.g., PEP 8 for Python, Airbnb style guide for JavaScript).

### Pull Request Process

Create a pull request for each feature or bug fix.  Ensure that all tests pass before merging.

### Issue Reporting

Report issues using the project's issue tracker. Provide clear descriptions and steps to reproduce the issue.


This comprehensive guide should help developers get started quickly and efficiently with `project-build-a-modern`. Remember to consult the project's specific documentation and README for more details.
