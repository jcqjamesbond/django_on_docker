web: gunicorn config.wsgi:application
worker: celery worker --app=interview_task.taskapp --loglevel=info
