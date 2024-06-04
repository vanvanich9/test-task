.PHONY: help install isort lint test build run

help:
	@echo "Available commands:"
	@echo "  install: Install all libraries"
	@echo "  isort: Sort imports"
	@echo "  lint: Check script by flake8"
	@echo "  test: Run tests"
	@echo "  build: Build service"
	@echo "  run: Run service"


install:
	@echo "Install all project libraries..."
	@pip install -r requirements.txt -r tests/functional/requirements.txt flake8==7.0.0 isort==5.13.2

isort:
	@echo "Sorting..."
	@isort .

lint:
	@echo "Check lint..."
	@flake8 .

test:
	@echo "Run tests..."
	@docker compose -f tests/functional/docker-compose.yaml up --exit-code-from tests --build

build:
	@echo "Build service..."
	@docker compose -f docker-compose.yaml build

run:
	@echo "Run service..."
	@docker compose -f docker-compose.yaml up || true
