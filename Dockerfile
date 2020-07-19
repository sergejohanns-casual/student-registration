FROM python:3.8-slim
COPY . .
RUN pip install -r requirements.txt
WORKDIR /flaskr
EXPOSE 5000
CMD export FLASK_APP=student_registration.py && flask run
