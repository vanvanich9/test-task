# Preparing to run the service and tests

Copy the contents of the ```.env.example``` file and paste it into the newly created ```.env``` file in the project root folder

# Run service

- **Using makefile:** To run the service for the first time, write ```make run``` in the terminal. If you have changed the script and have already runned the application once, you need to rebuild it using the ```make build``` command in the terminal, and then also write ```make run``` in the terminal.

- **Without using makefile:** To run the service for the first time, write ``docker compose up`` in the terminal. If you have modified the script and have already run the application once, you need to start the service with the build flag with the following command ```docker compose up --build``` in the terminal.

# Run tests

- **Using makefile:** To run tests, write ```make test``` command in the terminal.

- **Without using makefile:** To run tests, write ```docker compose -f tests/functional/docker-compose.yaml up --exit-code-from tests --build``` command in the terminal.

# Lint & Isort

- **Using makefile:** To run linters and isort, you must first install all the libraries using the ```make install``` command in the terminal. After that, to run linters, we will write the ```make lint``` command in the terminal, to run isort, we will write the ```make isort``` command in the terminal.

- **Without using makefile:** To run linters and isort, you must first install all the libraries using the ```pip install -r requirements.txt -r tests/functional/requirements.txt flake8==7.0.0 isort==5.13.2``` command in the terminal. After that, to run linters, we will write the ```flake8 .``` command in the terminal, to run isort, we will write the ```isort .``` command in the terminal.

# Links

**Link to the service:** http://127.0.0.1:8000/

**Link to the Swagger:** http://127.0.0.1:8000/api/openapi