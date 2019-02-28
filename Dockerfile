FROM python:latest

# Update all packages
RUN apt update && apt dist-upgrade -y

# Copy our app into the container
COPY app/ /usr/src/app

# We'll run all commands from this directory from here onwards
WORKDIR /usr/src/app

# Make sure pip itself is up to date, then install our requirements
RUN pip install --upgrade pip \
&& pip install -r requirements.txt

# Set up a non-root user for security reasons
RUN useradd app -d /usr/src/app

# Switch to the user we created
USER app

# Run our app
EXPOSE 8000
CMD python manage.py makemigrations \
&& python manage.py migrate \
&& python manage.py loaddata loaddata.json \
&& gunicorn wsgi:application -b 0.0.0.0:8000 -w 4



