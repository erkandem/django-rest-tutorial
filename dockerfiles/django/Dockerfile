FROM python:3.6-slim
RUN apt-get update && apt-get install postgresql-client -y
ENV working_directory=/app
RUN mkdir -p $working_directory
WORKDIR $working_directory
# add the application root folder to the contaner
# depends on where this Dockerfile is stored
ADD requirements.txt $working_directory
RUN pip install -r requirements.txt
ADD .env.docker  $working_directory/.env

RUN mkdir $working_directory/tutorial
ADD tutorial $working_directory/tutorial/

RUN mkdir $working_directory/options_data
ADD options_data $working_directory/options_data/

RUN mkdir $working_directory/quickstart
ADD quickstart $working_directory/quickstart/

ADD wait-for-postgres.sh $working_directory
ADD manage.py $working_directory

RUN chmod +x wait-for-postgres.sh
#CMD ["ls", "-la"]
#CMD ["pwd"]
CMD ["./wait-for-postgres.sh","db","python","manage.py","runserver","0.0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker build -f dockerfiles/django/Dockerfile -t djrest_django_app .
# docker run -p 8000:8000 djrest_django_app
