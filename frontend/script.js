const API = "http://127.0.0.1:8000/tasks";

let editingId = null;
let tasksCache = [];

// Load all tasks
async function loadTasks() {
    const res = await fetch(`${API}/tasks_all`);
    const tasks = await res.json();
    tasksCache = tasks;

    const box = document.getElementById("tasks");
    box.innerHTML = "";

    // Новые задачи сверху
    tasks.reverse().forEach(t => {
        box.innerHTML += `
            <div class="task-card">
                <div class="task-title">${t.title}</div>
                <div class="task-desc">${t.description ?? ""}</div>
                <div class="task-status">Completed: ${t.is_completed}</div>

                <div class="task-actions">
                    <span class="edit-btn" onclick="openEditor(${t.id})">Edit</span>
                    <span class="delete-btn" onclick="deleteTask(${t.id})">Delete</span>
                </div>
            </div>
        `;
    });
}

// Add task
async function addTask() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    if (!title.trim()) return alert("Please enter a title");

    await fetch(`${API}/add_tasks`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ title, description })
    });

    document.getElementById("title").value = "";
    document.getElementById("description").value = "";

    loadTasks();
}

// Delete task
async function deleteTask(id) {
    await fetch(`${API}/delete/${id}`, { method: "DELETE" });
    loadTasks();
}

// Open editor
function openEditor(id) {
    const task = tasksCache.find(t => t.id === id);
    if (!task) return;

    editingId = id;

    document.getElementById("editTitle").value = task.title;
    document.getElementById("editDescription").value = task.description ?? "";
    document.getElementById("editCompleted").checked = task.is_completed;

    document.getElementById("editor").classList.remove("hidden");
}

// Save editor
async function saveEditedTask() {
    const title = document.getElementById("editTitle").value;
    const description = document.getElementById("editDescription").value;
    const is_completed = document.getElementById("editCompleted").checked;

    await fetch(`${API}/update/${editingId}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ title, description, is_completed })
    });

    closeEditor();
    loadTasks();
}

// Close editor
function closeEditor() {
    document.getElementById("editor").classList.add("hidden");
    editingId = null;
}

loadTasks();
