class Task:
    def __init__(self, task_id, title,assignee,priority="Minor",reporter="Admin", description="", status="To Do"):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.assignee = assignee
        self.status = status
        self.reporter = reporter
        self.description = description

    def update_status(self, new_status):
        """Метод за промяна на статуса на задачата."""
        valid_statuses = ["To Do", "In Progress", "Done"]
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False

    def get_details(self):
        """Метод за връщане на форматирана информация."""
        return f"[{self.task_id}] {self.title}  Status: {self.status} - Assigned to: {self.assignee}"