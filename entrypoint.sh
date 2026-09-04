#!/bin/bash
set -e
pytest -v --tb=no -o log_cli=true -n auto --alluredir=artifacts/allure-results