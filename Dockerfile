FROM python:3.8-alpine
WORKDIR /jenkins_docker_test
COPY test.py /jenkins_docker_test
CMD ["test.py"]
ENTRYPOINT [ "python3" ]