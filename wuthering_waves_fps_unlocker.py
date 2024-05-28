import json
import os
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox


def select_launcher():
    file_path = filedialog.askopenfilename(title="请选择鸣潮启动器", filetypes=[("Executable Files", "*.exe")])
    if file_path:
        # 获取launcher.exe所在目录
        base_dir = os.path.dirname(file_path)
        local_storage_path = os.path.join(base_dir, "Wuthering Waves Game", "Client", "Saved", "LocalStorage",
                                          "LocalStorage.db")
        if os.path.exists(local_storage_path):
            modify_frame_rate(local_storage_path)
        else:
            messagebox.showerror("错误", "找不到文件！")


def modify_frame_rate(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT value FROM LocalStorage WHERE key = 'GameQualitySetting'")
        result = cursor.fetchone()

        if result:
            settings = json.loads(result[0])
            settings["KeyCustomFrameRate"] = 120
            new_value = json.dumps(settings)

            cursor.execute("UPDATE LocalStorage SET value = ? WHERE key = 'GameQualitySetting'", (new_value,))
            conn.commit()
            messagebox.showinfo("修改完成", "帧率上限已设置为120")
        else:
            messagebox.showerror("错误", "找不到设置项！")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if conn:
            conn.close()


app = tk.Tk()
app.title("一键设置鸣潮帧率上限至120")
app.geometry("400x225")

select_button = tk.Button(app, text="请选择鸣潮启动器", command=select_launcher)
select_button.pack(pady=20)

app.mainloop()
