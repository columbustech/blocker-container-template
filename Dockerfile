FROM python:3

RUN apt-get update && apt-get install -y vim

WORKDIR /blockfn/src
COPY src .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "3600", "--error-logfile", "-", "--access-logfile", "-", "--log-level", "info", "blocker.wsgi"]
#CMD python manage.py runserver 0.0.0.0:8000
#CMD ["sh", "-c", "/bin/bash"]
