# Mini Jira Board

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)

**Mini Jira Board** е леко и бързо уеб приложение за управление на работния процес (Task Management). Проектът имплементира Kanban методология за проследяване на задачи, разпределени в различни етапи на изпълнение.

---
## Архитектурни решения

- **Data Persistence Strategy**: Приложението използва **Stateless** архитектура.
- **In-Memory State Management**: Състоянието на обектите се съхранява в глобален динамичен списък (`list`) в оперативната памет. Това позволява мигновена обработка на данните, като същевременно демонстрира управление на жизнения цикъл на обекти в реално време.
- **Data Encapsulation**: Всеки тикет е инстанция на класа `Task`, което гарантира, че бизнес логиката (като промяна на статус и валидация на приоритет) е капсулирана в самия модел, а не в контролера.

---

## Технологичен стек

- **Core:** [Python 3.x](https://www.python.org/)
- **Web Framework:** [Flask](https://flask.palletsprojects.com/)
- **Templating Engine:** Jinja2
- **Frontend:** HTML5, CSS3 (Custom Modular CSS)

##  Функционалности

- **Dynamic Board**: Интуитивно разпределение на задачите в колони `To Do`, `In Progress` и `Done`.
- **Task Lifecycle Management**: Лесно преместване на задачите между отделните статуси.
- **Priority Filtering**: Вградена система за филтриране на задачите по приоритет в реално време (Critical/Bug, Major, Minor).
- **CRUD Operations**: Поддръжка за създаване,редактиране, четене и изтриване на тикети.
- **Modular Design**: Разделена логика между моделите (Data Layer) и маршрутите (Controller Layer).

![Main Board](screenshots/Screenshot_4.png)
![Create Task](screenshots/Screenshot_2.png)
![Edit Task](screenshots/Screenshot_3.png)
