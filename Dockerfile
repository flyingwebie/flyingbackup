FROM python:3.12

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install nginx vim net-tools

COPY ./nginx/default_80.conf /etc/nginx/sites-available/default

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /app
COPY . /code
COPY ./init.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/init.sh

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 80

#COPY ./init.sh /usr/local/bin/init.sh
#RUN chmod a+x /usr/local/bin/init.sh
#RUN ls -lsa --color /usr/local/bin/

ENTRYPOINT ["init.sh"]
