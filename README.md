# Todo List

A Django-based Todo List application that allows users to manage tasks and organize them with tags.

## Features

- Display all tasks on the home page
- Sort tasks by completion status and creation date
- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Undo completed tasks
- Set optional task deadlines
- Create, update and delete tags
- Assign multiple tags to tasks
- Display task creation date and deadline
- Responsive interface with Bootstrap
- Shared sidebar navigation across all pages

## Task Model

Each task contains:

- Content
- Creation date and time
- Optional deadline
- Completion status
- Multiple tags

## Tag Model

Each tag contains:

- Name

A task can have multiple tags, and a tag can be assigned to multiple tasks.

## Technologies

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap

## Project Structure

```text
py-todo-list/
├── todo/
│   ├── migrations/
│   ├── static/
│   │   └── todo/
│   │       └── styles.css
│   ├── templates/
│   │   ├── includes/
│   │   │   └── sidebar.html
│   │   ├── base.html
│   │   └── todo/
│   │       ├── tag_confirm_delete.html
│   │       ├── tag_form.html
│   │       ├── tag_list.html
│   │       ├── task_confirm_delete.html
│   │       ├── task_form.html
│   │       └── task_list.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── .gitignore
├── .flake8
├── manage.py
└── README.md

