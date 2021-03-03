FROM python:3.6

WORKDIR /test_gdc

COPY /test_gdc .

RUN apt-get update && apt-get install -y unixodbc-dev && apt-get install vim -y

RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
CMD python csv_to_sql.py -u root -p RootPassword
