#!/usr/bin/env bash

# Exit on error
set -o errexit

# Package manager
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Database migrations
python manage.py migrate