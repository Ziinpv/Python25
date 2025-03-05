import tkinter as tk
from tkinter import messagebox, simpledialog

# Hàm thêm công việc mới
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Hàm xóa công việc đã chọn
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

# Hàm chỉnh sửa công việc
def edit_task():
    try:
        index = listbox.curselection()
        current_task = listbox.get(index)
        new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=current_task)
        
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit!")

# Hàm đánh dấu công việc là đã hoàn thành
def mark_completed():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(index, task + " (Completed)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed!")

# Hàm lưu danh sách công việc vào file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Save", "Tasks saved successfully!")

# Hàm tải danh sách công việc từ file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Load Error", "No saved tasks found!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("To-Do List")

# Thiết lập giao diện
root.config(bg="#f0f8ff")
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

entry = tk.Entry(frame, width=40, font=("Arial", 12), bd=2, relief="solid")
entry.pack(side=tk.LEFT, padx=10, pady=5)

add_button = tk.Button(frame, text="Add Task", width=15, font=("Arial", 12), bg="#4CAF50", fg="white", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox để hiển thị các công việc
listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12), selectmode=tk.SINGLE, bd=2, relief="solid", bg="#e6f7ff")
listbox.pack(pady=10)

# Các nút chức năng
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack()

delete_button = tk.Button(button_frame, text="Delete Task", width=20, font=("Arial", 12), bg="#f44336", fg="white", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Mark as Completed", width=20, font=("Arial", 12), bg="#ff9800", fg="white", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task", width=20, font=("Arial", 12), bg="#2196F3", fg="white", command=edit_task)
edit_button.pack(side=tk.LEFT, padx=5)

# Thêm các nút lưu và tải danh sách
save_button = tk.Button(button_frame, text="Save Tasks", width=20, font=("Arial", 12), bg="#8bc34a", fg="white", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(button_frame, text="Load Tasks", width=20, font=("Arial", 12), bg="#03a9f4", fg="white", command=load_tasks)
load_button.pack(side=tk.LEFT, padx=5)

# Tải danh sách công việc khi mở ứng dụng
load_tasks()

# Chạy ứng dụng
root.mainloop()
