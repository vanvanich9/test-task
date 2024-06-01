#!/usr/bin/env bash

python ./wait_for_service.py
pytest --confcutdir=/tests/functional /tests/functional/src