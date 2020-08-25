FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /library

# Set the working directory to /library
WORKDIR /library

# Copy the current directory contents into the container at /library
ADD . /library

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
