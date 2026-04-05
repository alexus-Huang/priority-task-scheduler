# Priority Task Scheduler (Custom Heap Implementation)

## 📌 Overview

This project is a command-line **Task Scheduler** built using core Data Structures and Algorithms concepts. It prioritizes tasks based on urgency using a **custom Max-Heap implementation**, ensuring efficient task management.

Unlike basic to-do lists, this system always retrieves the **highest-priority task first**, mimicking how operating systems schedule processes.

---

## 🚀 Features

* Add tasks with priority levels (1–10)
* Retrieve the highest-priority task instantly
* Remove (complete) tasks from the system
* Handle multiple tasks efficiently using a heap
* (Optional) FIFO handling for equal priorities using a queue

---

## 🧠 Data Structures Used

### 1. Max Heap

* Stores tasks based on priority
* Ensures highest-priority task is always at the root

**Time Complexity:**

* Insert: `O(log n)`
* Extract Max: `O(log n)`
* Peek: `O(1)`

---

### 2. Queue (Extension Feature)

* Used for handling tasks with equal priority
* Maintains **first-in, first-out (FIFO)** order

---

## 🏗️ Project Structure

```
priority-task-scheduler/
│
├── main.py              # Entry point / CLI interface
├── max_heap.py          # Custom heap implementation
├── task.py              # Task class definition
└── README.md
```

---

## 💻 How It Works

1. User adds a task with a priority
2. Task is inserted into the Max Heap
3. Heap organizes tasks automatically
4. When retrieving a task:

   * The highest-priority task is returned first
   * If priorities are equal → queue determines order

---

## ▶️ Example Usage

```
1. Add Task
2. View Next Task
3. Complete Task
4. Exit
```

Example:

```
Add Task: Homework (Priority 5)
Add Task: Project (Priority 8)

Next Task → Project
```

---

## 🧪 What I Learned

* How heaps work internally (array-based tree structure)
* Implementing heap operations from scratch:

  * Heapify Up
  * Heapify Down
* Time complexity tradeoffs in real systems
* Combining multiple data structures (Heap + Queue)

---

## 🔥 Future Improvements

* Add due dates and scheduling
* Build a GUI (Tkinter or web app)
* Store tasks persistently (file/database)
* Add sorting by deadline + priority

---

## 📚 Why This Project Matters

This project demonstrates practical understanding of:

* Data Structures & Algorithms
* Problem decomposition
* Writing clean, structured code

It goes beyond using built-in libraries by implementing core logic from scratch.

---

## 🛠️ Tech Stack

* Python
* Core DSA (Heap, Queue)

---

## 👤 Author

Built as a DSA practice project to strengthen understanding of heaps and priority queues.
