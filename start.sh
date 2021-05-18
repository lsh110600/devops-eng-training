#!/bin/bash

python app.py
pytest unittest/functions_test.py
pytest integration/app_test.py
