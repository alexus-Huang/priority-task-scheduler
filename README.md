# Priority Task Manager

A robust Python-based task management system that utilizes a custom **Max-Heap** to ensure tasks are processed according to their importance. 

## 📌 Project Overview
This project manages tasks based on a dual-priority system:
1.  **Priority Level:** Tasks with higher priority values (e.g., 10) are handled first.
2.  **Order of Insertion:** If two tasks have the same priority, the one added first is given precedence (FIFO).

## 📂 File Structure
* `task.py`: Defines the `Task` object and custom comparison logic for the heap.
* `max_heap.py`: A manual implementation of a Max-Heap data structure (without using built-in libraries like `heapq`).
* `main.py`: The user interface and demonstration script to manage the task queue.

## 🚀 Key Features
* **Dynamic Heapification:** Automatically reorganizes the queue when tasks are added or completed.
* **Peek Functionality:** View the current highest-priority task without removing it.
* **Specific Removal:** Allows removing a task by name while maintaining the heap's structural integrity.
* **Tie-Breaking Logic:** Uses an `order_counter` to ensure fairness among tasks with equal priority.

## ⚙️ How It Works
The core logic resides in `max_heap.py`, which uses a binary tree represented as an array:
* **`_heapify_up`**: Moves a new task up the tree until it reaches its correct priority level.
* **`_heapify_down`**: Re-balances the tree after the top task is completed or a specific task is removed.

## 🧪 What I Learned
* **Internal Heap Mechanics:** Understood how to represent a tree structure using an array/list.
* **Manual Implementation:** Gained hands-on experience writing `Heapify Up` and `Heapify Down` logic from scratch.
* **Root Preservation:** Learned the importance of saving the root value in a temporary variable before overwriting it during extraction, ensuring the maximum value is successfully returned after the heap is restructured.
* **System Trade-offs:** Explored time complexity tradeoffs in real-world systems and the benefits of combining data structures (Heap + Queue logic).

## 🛠 Usage
To run the project, ensure you have Python installed and run the main script:

```bash
python main.py