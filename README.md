under project root directory, run the following command to build the development environment
docker-compose -f local.yml build
run the following to run locally:
docker-compose -f local.yml up
run the following command to take unit testing:
docker-compose -f local.yml run django py.test

costume API is implemented under config/urls.py, relevant views.py is under router/views.py
unit test code is under interview_task/users/tests/test_urls.py
