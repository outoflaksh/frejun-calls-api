#!/bin/bash

RUN_PORT=${PORT:-8000}

gunicorn src.api:app -b '0.0.0.0':${RUN_PORT}