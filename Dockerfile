FROM python:3.8-slim
COPY . .
RUN pip install -r requirements.txt
WORKDIR /flaskr
RUN python3 make_test_data.py
EXPOSE 5000
CMD export FLASK_APP=student_registration.py && flask run --host=0.0.0.0
