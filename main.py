from flask import Flask, render_template, request, redirect, url_for
from models import Task

app = Flask(__name__)

tasks_db = [
    Task(1, "Fix Login Bug", "Ivanka"),
    Task(2, "Create API Docs", "Aleksandra")
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
    if title:
        new_id = len(tasks_db) + 1
        new_task = Task(new_id, title, assignee, priority)
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



if __name__ == '__main__':
    app.run(debug=True)
