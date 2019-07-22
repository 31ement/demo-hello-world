FROM python:3
ADD demo-hello-world.py /
RUN pip install flask
EXPOSE 5000
CMD [ "python", "./demo-hello-world.py" ]
