# syntax=docker/dockerfile:1
# https://blog.logrocket.com/build-deploy-flask-app-using-docker/
# https://medium.com/@law01f/flask-over-https-cd9826102c65
# https://stackoverflow.com/questions/29458548/can-you-add-https-functionality-to-a-python-flask-web-server
# https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
FROM python:3.9.20-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# ENTRYPOINT [ "python3" ]
CMD [ "python3", "main.py"]