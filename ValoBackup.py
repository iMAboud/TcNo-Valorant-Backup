import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from datetime import datetime

# List of directories to backup and restore
directories_to_backup = {
    "TcNo Account Switcher": os.path.join(os.getenv("USERPROFILE"), "AppData", "Roaming", "TcNo Account Switcher"),
    "Riot Games": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Riot Games"),
    "VALORANT": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "VALORANT"),
}

def backup():
    today = datetime.now()
    suggested_filename = f"ValorantBackup | {today.strftime('%d-%m')}.zip"
    zip_filename = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")], initialfile=suggested_filename)
    
    if zip_filename:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder_name, source_dir in directories_to_backup.items():
                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            zipf.write(file_path, os.path.relpath(file_path, os.getenv("USERPROFILE")))
                        except PermissionError:
                            print(f"Permission denied: {file_path}, skipping...")  
        messagebox.showinfo("Backup", "Backup completed successfully!")

def restore():
    userprofile = os.getenv("USERPROFILE")
    zip_filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    
    if zip_filename:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(userprofile)
        messagebox.showinfo("Restore", "Restore completed successfully!")

class BackupRestoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Valorant Backup & Restore")
        self.root.geometry("500x400")
        self.root.configure(bg="#2E2E2E")
        
        close_button = tk.Button(self.root, text="X", command=self.root.quit, fg="white", bg="#FF6347", font=("Arial", 12, "bold"), bd=0, relief="flat", highlightthickness=0)
        close_button.place(relx=1.0, x=-10, y=10, anchor='ne')
        
        self.img = Image.open(r"valorant.ico")
        original_width, original_height = self.img.size
        aspect_ratio = original_width / original_height
        new_width = 200
        new_height = int(new_width / aspect_ratio)
        self.img = self.img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        
        img_label = tk.Label(self.root, image=self.img, bg="#2E2E2E")
        img_label.pack(pady=20)
        
        backup_button = tk.Button(self.root, text="Backup", command=backup, fg="white", bg="#1E90FF", font=("Arial", 12, "bold"), bd=0, relief="flat", highlightthickness=0)
        backup_button.pack(pady=10)
        backup_button.bind("<Enter>", lambda e: backup_button.config(bg="#4169E1"))
        backup_button.bind("<Leave>", lambda e: backup_button.config(bg="#1E90FF"))
        
        restore_button = tk.Button(self.root, text="Restore", command=restore, fg="white", bg="#32CD32", font=("Arial", 12, "bold"), bd=0, relief="flat", highlightthickness=0)
        restore_button.pack(pady=10)
        restore_button.bind("<Enter>", lambda e: restore_button.config(bg="#2E8B57"))
        restore_button.bind("<Leave>", lambda e: restore_button.config(bg="#32CD32"))

if __name__ == "__main__":
    root = tk.Tk()
    app = BackupRestoreApp(root)
    root.mainloop()
