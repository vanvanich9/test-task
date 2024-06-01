.PHONY: help install isort style test build run

help:
	@echo "Available commands:"
	@echo "  install: Install all libraries"
	@echo "  isort: Check sort of imports"
	@echo "  style: Check script to style"
	@echo "  test: Run tests"
	@echo "  build: Build service"
	@echo "  run: Run service"


install:
	@echo "Install all project libraries..."
	@pip install -r requirements.txt
	@pip install -r tests/functional/requirements.txt
	@pip install flake8==7.0.0 isort==5.13.2

isort: install
	@echo "Check isort..."
	@isort .

style: install
	@echo "Check style..."
	@flake8 .

test:
	@echo "Run tests..."
	@docker compose -f tests/functional/docker-compose.yaml rm --force --stop
	@docker compose -f tests/functional/docker-compose.yaml up --exit-code-from tests --build

build:
	@echo "Build service..."
	@docker compose -f docker-compose.yaml rm --force --stop
	@docker compose -f docker-compose.yaml build

run:
	@echo "Run service..."
	@docker compose -f docker-compose.yaml up || true
