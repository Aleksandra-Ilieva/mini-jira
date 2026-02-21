from flask import Flask, render_template, request, redirect, url_for
from models import Task

app = Flask(__name__)

tasks_db = [
    Task(
        task_id=1,
        title="Fix Login Bug",
        priority="Critical/Bug",
        assignee="Mihaela",
        reporter="Georgi",
        description="Users cannot log in with Google accounts. Shows 404 error."
    ),
    Task(
        task_id=2,
        title="Create API Docs",
        priority="Major",
        assignee="Aleksandra",
        reporter="Ivan",
        description="Document all endpoints for the new user module."
    )
]


@app.route('/')
def index():
    selected_priority = request.args.get('priority')

    filtered_tasks = tasks_db

    if selected_priority and selected_priority != "All":
        filtered_tasks = [task for task in tasks_db if task.priority == selected_priority]

    sorted_tasks = sorted(filtered_tasks, key=lambda x: x.task_id)

    return render_template('index.html', tasks=sorted_tasks, current_priority=selected_priority)


@app.route('/create-task')
def create_task():
    return render_template('create-task.html')


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    priority = request.form.get('priority')
    assignee = request.form.get('assignee')
    reporter = request.form.get('reporter')
    description = request.form.get('description')
    if title:
        new_id = len(tasks_db) + 1
        new_task = Task(
            task_id=new_id,
            title=title,
            assignee=assignee,
            priority=priority,
            reporter=reporter,
            description=description
        )
        tasks_db.append(new_task)
    return redirect(url_for('index'))


@app.route('/move/<int:task_id>/<string:next_status>')
def move_task(task_id, next_status):
    for task in tasks_db:
        if task.task_id == task_id:
            task.update_status(next_status)
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks_db
    tasks_db = [task for task in tasks_db if task.task_id != task_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET'])
def edit_task_page(task_id):
    task_to_edit = next((t for t in tasks_db if t.task_id == task_id), None)
    if task_to_edit:
        return render_template('edit-task.html', task=task_to_edit)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    for task in tasks_db:
        if task.task_id == task_id:
            task.title = request.form.get('title')
            task.priority = request.form.get('priority')
            task.assignee = request.form.get('assignee')
            task.reporter = request.form.get('reporter')
            task.description = request.form.get('description')
            break
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
