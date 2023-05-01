FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./ /app

#TODO чтобы зависимости кэшировались
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]