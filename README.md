
И API для задач должны быть такими:

| Метод | Endpoint               | Описание            |
|-------|-------------------------|----------------------|
| GET   | /tasks/tasks_all        | Получить все задачи |
| POST  | /tasks/add_tasks        | Создать задачу      |
| PUT   | /tasks/update/{id}      | Обновить задачу     |
| DELETE| /tasks/delete/{id}      | Удалить задачу      |

Если у тебя другой URL, измени строку в `script.js`:

```js
const API = "http://127.0.0.1:8000/tasks";
