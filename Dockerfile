FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./ /app
WORKDIR /app

RUN apt update && apt install  -y curl unzip xvfb libxi6 libgconf-2-4 default-jdk chromium

#TODO чтобы зависимости кэшировались
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]