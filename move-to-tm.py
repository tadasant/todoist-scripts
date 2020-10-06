import os
from todoist.api import TodoistAPI

todoist_api_key = os.environ["TODOIST_API_KEY"]

api = TodoistAPI(todoist_api_key)
api.sync()
print(api.state["projects"])
