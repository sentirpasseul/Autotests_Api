FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN rm -rf artifacts && mkdir -p artifacts/logs artifacts/allure-results


CMD ["pytest", "-v", "--tb=no", "-o", "log_cli=true", "-n", "auto", "--alluredir=artifacts/allure-results"]

