FROM python

WORKDIR /usr/src/app

RUN python -m pip install Django

# RUN apt-get install sqlite3

COPY . .

EXPOSE 8000

CMD ["python", "djangoapp/manage.py", "runserver", "0.0.0.0:8000"]