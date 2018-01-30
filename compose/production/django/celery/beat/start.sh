#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A interview_task.taskapp beat -l INFO
