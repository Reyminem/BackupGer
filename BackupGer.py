import tkinter as tk
from tkinter import ttk
import configparser
import subprocess
import functools
import os
import shutil
import sys
import ctypes
import tempfile

# Personalização do programa e da janela
app = tk.Tk()
app.title("BackupGer")
app.geometry("400x400")
icon_path = os.path.join(os.path.dirname(__file__), "bin", "12.ico")
app.iconbitmap(icon_path)

# Carrega a .dll pro funcionamento no Windows 7
exe_directory = os.path.dirname(sys.executable)
dll_path = os.path.join(exe_directory, "bin", "api-ms-win-core-path-l1-1-0.dll")
try:
    dll = ctypes.WinDLL(dll_path)
except OSError as e:
    print(f"Erro ao carregar a DLL: {e}")

# Aplica o tema "clam"
style = ttk.Style()
style.theme_use("clam")

# Widget para criação de um app com várias abas
notebook = ttk.Notebook(app)
notebook.pack(pady=0, fill='both', expand=True)

# Aba de configurações
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Config")

# Função para salvar dados do servidor SQL
def save_id():
    if not (id_entry.get()):
        status_label.config(text="Erro: preencha todos os campos!", foreground="red")
        return
    
    class NoSpaceConfigParser(configparser.RawConfigParser):
        def write(self, fp, space_around_delimiters=False):
            super().write(fp, space_around_delimiters=False)
    
    config = NoSpaceConfigParser()
    config['ID'] = {
        'id_cliente': id_entry.get()
    }

    save_directory = "C:\BKP_1.2"
    os.makedirs(save_directory, exist_ok=True)
    
    file_path = os.path.join(save_directory, "id.ini")
    
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    status_label_tab2.config(text="Salvo com sucesso!", foreground="green")

title_label_tab2 = ttk.Label(tab1, text="ID do Cliente", font=("Helvetica", 12, "bold"))
title_label_tab2.pack(pady=10)

id_entry = ttk.Entry(tab1)
id_entry.pack(pady=2)

save_button = ttk.Button(tab1, text="Salvar ID", command=save_id)
save_button.pack(pady=10)

title_label_tab2 = ttk.Label(tab1, text="Instalar 7-Zip", font=("Helvetica", 12, "bold"))
title_label_tab2.pack(pady=10)

# Caminho para os executáveis 7-Zip no diretório bin
seven_zip_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")

# Função para executar o 7z.exe
def executar_7z():
    try:
        # Cria um diretório temporário para evitar problemas de permissão
        temp_dir = tempfile.mkdtemp()
        
        # Copia o 7z.exe para o diretório temporário
        shutil.copy2(os.path.join(seven_zip_dir, "7z.exe"), temp_dir)

        # Executa o 7z.exe a partir do diretório temporário
        subprocess.run([os.path.join(temp_dir, "7z.exe")])

        # Remove o diretório temporário após a execução
        shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Erro ao executar 7z.exe: {e}")

# Função para executar o 7z-x64.exe
def executar_7z_x64():
    try:
        # Cria um diretório temporário para evitar problemas de permissão
        temp_dir = tempfile.mkdtemp()
        
        # Copia o 7z-x64.exe para o diretório temporário
        shutil.copy2(os.path.join(seven_zip_dir, "7z-x64.exe"), temp_dir)

        # Executa o 7z-x64.exe a partir do diretório temporário
        subprocess.run([os.path.join(temp_dir, "7z-x64.exe")])

        # Remove o diretório temporário após a execução
        shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Erro ao executar 7z-x64.exe: {e}")

# Frame para os botões de criação de rotina
sevenzip_frame = ttk.Frame(tab1)
sevenzip_frame.pack(padx=15, pady=5)

# Cria um botão para executar o 7z.exe
button_7z = ttk.Button(sevenzip_frame, text="32 Bits", command=executar_7z)
button_7z.grid(row=0, column=0, padx=10, pady=5)

# Cria um botão para executar o 7z-x64.exe
button_7z_x64 = ttk.Button(sevenzip_frame, text="64 Bits", command=executar_7z_x64)
button_7z_x64.grid(row=0, column=1, padx=10, pady=5)

status_label_tab1 = ttk.Label(tab1, text="", foreground="black")
status_label_tab1.pack()

# Aba de diretórios MySQL
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="MySQL")

# Título
title_label_tab2 = ttk.Label(tab2, text="Criação de Diretórios MySQL", font=("Helvetica", 12, "bold"))
title_label_tab2.pack(pady=5)

# Função para criação dos diretórios
def create_directories():
    base_path = "C:\\BKP_1.2"
    subdirectories = ["ScriptsMySQL", "Backup\\Domingo", "Backup\\Almoco", "Backup\\Segunda", "Backup\\Terca",
                      "Backup\\Quarta", "Backup\\Quinta", "Backup\\Sexta", "Backup\\Sabado"]

    for directory in subdirectories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    base_path_2 = "C:\\Program Files (x86)\\12informatica\\BackupDrive"
    subdirectories_2 = ["Domingo", "Almoco", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]

    for directory in subdirectories_2:
        os.makedirs(os.path.join(base_path_2, directory), exist_ok=True)

    # Copia os arquivos da pasta "Scripts" para "C:\BKP_1.2\Scripts"
    script_target_dir = "C:\\BKP_1.2\\ScriptsMySQL"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_source_dir = os.path.join(script_dir, "ScriptsMySQL")

    for item in os.listdir(scripts_source_dir):
        source_item = os.path.join(scripts_source_dir, item)
        target_item = os.path.join(script_target_dir, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, target_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, target_item)

    status_label_tab2.config(text="Diretórios e arquivos criados com sucesso!", foreground="green")

create_directories_button = ttk.Button(tab2, text="Criar diretórios", command=create_directories)
create_directories_button.pack(pady=10)

status_label_tab2 = ttk.Label(tab2, text="", foreground="black")
status_label_tab2.pack()

# Criação de rotinas MySQL
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Rotinas MySQL")

# Título
title_label_tab3 = ttk.Label(tab3, text="Rotinas MySQL", font=("Helvetica", 12, "bold"))
title_label_tab3.pack(pady=5)

# Caixas de seleção para os dias
days_label = ttk.Label(tab3, text="Selecione os dias:")
days_label.pack(pady=1)

# Traduz os dias para português
day_translation = {
    "Sun": "Dom",
    "Mon": "Seg",
    "Tue": "Ter",
    "Wed": "Qua",
    "Thu": "Qui",
    "Fri": "Sex",
    "Sat": "Sáb",
    "Lunch": "Alm",
}

# Legenda para os botões dos dias
day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
day_labels.append("Lunch")
selectedmysql_day_var = tk.StringVar()

# Função para a seleção dos dias
def select_daymysql(day, button):
    selectedmysql_days = selectedmysql_day_var.get().split(",")

    if day in selectedmysql_days:
        selectedmysql_days.remove(day)
        translated_day = day_translation[day]
        button.config(text=f"{translated_day} ☐")
    else:
        selectedmysql_days.append(day)
        translated_day = day_translation[day]
        button.config(text=f"{translated_day} ☑")

    selectedmysql_day_var.set(",".join(selectedmysql_days))

# Frame para os botões
day_buttons_frame = ttk.Frame(tab3)
day_buttons_frame.pack(padx=15, pady=2)

# Loop para a criação dos botões
day_buttons = []

for i in range(8):
    row = i // 2
    col = i % 2

    translated_day = day_translation[day_labels[i]]
    day_button_text = f"{translated_day} ☐ "
    day_button = ttk.Button(day_buttons_frame, text=day_button_text)
    day_button.grid(row=row, column=col, padx=5, pady=5)
    day_buttons.append(day_button)

    day_label = day_labels[i]
    translated_day_label = day_translation[day_label]
    day_button.config(command=functools.partial(select_daymysql, day_label, day_button))

# Caixa para a entrada do horário
hour_label = ttk.Label(tab3, text="Hora:")
hour_label.pack()

hour_var = tk.StringVar(tab3, value="16:30") # Placeholder
hour_entry = ttk.Entry(tab3, textvariable=hour_var)
hour_entry.pack()

# Caixa para a entrada do horário do almoço
lunch_hour_label = ttk.Label(tab3, text="Horário do Almoço:")
lunch_hour_label.pack()

lunch_var = tk.StringVar(tab3, value="12:00") # Placeholder
lunch_hour_entry = ttk.Entry(tab3, textvariable=lunch_var)
lunch_hour_entry.pack()

mysql_bat_files = {
    "Lunch": "C:\BKP_1.2\ScriptsMySQL\BKPAlmoco.bat",
    "Sun": "C:\BKP_1.2\ScriptsMySQL\BKPDomingo.bat",
    "Mon": "C:\BKP_1.2\ScriptsMySQL\BKPSegunda.bat",
    "Tue": "C:\BKP_1.2\ScriptsMySQL\BKPTerca.bat",
    "Wed": "C:\BKP_1.2\ScriptsMySQL\BKPQuarta.bat",
    "Thu": "C:\BKP_1.2\ScriptsMySQL\BKPQuinta.bat",
    "Fri": "C:\BKP_1.2\ScriptsMySQL\BKPSexta.bat",
    "Sat": "C:\BKP_1.2\ScriptsMySQL\BKPSabado.bat",
}

# Função para criação das rotinas
def create_mysqltask():
    selected_days = selectedmysql_day_var.get().split(",")
    selected_hour = hour_var.get()

    for selected_day in selected_days:
        if selected_day in mysql_bat_files:
            batch_file_path = mysql_bat_files[selected_day]
            translated_day = day_translation[selected_day]
            task_name = f"MySQL {translated_day}"
            task_command = [
                "schtasks", "/create", "/tn", task_name, "/tr", batch_file_path,
                "/sc", "weekly", "/d", selected_day, "/st", selected_hour, "/f",
                "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
            ]

            # Condição para a rotina do almoço
            if selected_day == "Lunch":
                lunch_hour = lunch_hour_entry.get()
                lunch_task_name = f"MySQL {translated_day}"
                lunch_task_command = [
                    "schtasks", "/create", "/tn", lunch_task_name, "/tr", batch_file_path,
                    "/sc", "daily", "/st", lunch_hour_entry.get(), "/f",
                    "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
                ]
                subprocess.run(lunch_task_command, capture_output=True, text=True)

            else:
                # Cria a tarefa normalmente para os outros dias
                subprocess.run(task_command, capture_output=True, text=True)

            status_label_tab3.config(text="Rotinas MySQL criadas!", foreground="blue")
        else:
            status_label_tab3.config(text=f"Nenhum dia selecionado!", foreground="red")

# Botão para a criação da rotina de scan para verificação
def create_startup_routine():
    batch_file_path = "C:\BKP_1.2\ScriptsMySQL\BackupVerif.exe"
    task_name = "MySQL Verifica"
    task_command = [
        "schtasks", "/create", "/tn", task_name, "/tr", batch_file_path,
        "/sc", "onstart", "/f", "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
    ]
    subprocess.run(task_command, capture_output=True, text=True)
    status_label_tab3.config(text="Rotina de verificação criada!", foreground="blue")

# Frame para os botões de criação de rotina
create_buttons_frame = ttk.Frame(tab3)
create_buttons_frame.pack(padx=15, pady=2)

# Botão para criar tarefas
create_mysqltask_button = ttk.Button(create_buttons_frame, text="Criar tarefas", command=create_mysqltask)
create_mysqltask_button.grid(row=0, column=0, padx=10, pady=5)

# Botão para criar a rotina de scan para envio de e-mail
create_startup_routine_button = ttk.Button(create_buttons_frame, text="Rotina de verificação", command=create_startup_routine)
create_startup_routine_button.grid(row=0, column=1, padx=10, pady=5)

status_label_tab3 = ttk.Label(tab3, text="", foreground="black")
status_label_tab3.pack()

# Diretórios SQL
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="SQL")

title_label_tab4 = ttk.Label(tab4, text="Criação de Diretórios SQL", font=("Helvetica", 12, "bold"))
title_label_tab4.pack(pady=5)

def create_directories():
    base_path = "C:\\BKP_1.2"
    subdirectories = ["ScriptsSQL", "Backup\\Domingo", "Backup\\Almoco", "Backup\\Segunda", "Backup\\Terca",
                      "Backup\\Quarta", "Backup\\Quinta", "Backup\\Sexta", "Backup\\Sabado"]

    for directory in subdirectories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    base_path_2 = "C:\\Program Files (x86)\\12informatica\\BackupDrive"
    subdirectories_2 = ["Domingo", "Almoco", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]

    for directory in subdirectories_2:
        os.makedirs(os.path.join(base_path_2, directory), exist_ok=True)

    # Copia os arquivos da pasta "ScriptsSQL" para "C:\BKP_1.2\ScriptsSQL"
    script_target_dir = "C:\\BKP_1.2\\ScriptsSQL"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_source_dir = os.path.join(script_dir, "ScriptsSQL")

    try:
        for item in os.listdir(scripts_source_dir):
            source_item = os.path.join(scripts_source_dir, item)
            target_item = os.path.join(script_target_dir, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, target_item)

        status_label.config(text="Diretórios e arquivos criados com sucesso!", foreground="green")
    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}", foreground="red")        

    temp_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)

create_directories_button = ttk.Button(tab4, text="Criar diretórios", command=create_directories)
create_directories_button.pack(pady=10)

# Função para salvar dados do servidor SQL
def save_data():
    if not (server_name_entry.get() and user_entry.get() and password_entry.get()):
        status_label.config(text="Erro: preencha todos os campos!", foreground="red")
        return
    
    class NoSpaceConfigParser(configparser.RawConfigParser):
        def write(self, fp, space_around_delimiters=False):
            super().write(fp, space_around_delimiters=False)
    
    config = NoSpaceConfigParser()
    config['Server'] = {
        'Server': server_name_entry.get(),
        'User': user_entry.get(),
        'Password': password_entry.get()
    }

    save_directory = "C:\BKP_1.2\ScriptsSQL"
    os.makedirs(save_directory, exist_ok=True)
    
    file_path = os.path.join(save_directory, 'server.ini')
    
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    status_label.config(text="Salvo com sucesso!", foreground="green")

# Títulos para as caixas de entrada
server_name_label = ttk.Label(tab4, text="Servidor:")
server_name_label.pack(pady=2)
server_name_entry = ttk.Entry(tab4)
server_name_entry.pack(pady=2)

user_label = ttk.Label(tab4, text="Usuário:")
user_label.pack(pady=2)
user_entry = ttk.Entry(tab4)
user_entry.pack(pady=2)

password_label = ttk.Label(tab4, text="Senha:")
password_label.pack(pady=2)
password_entry = ttk.Entry(tab4, show='*')
password_entry.pack(pady=2)

save_button = ttk.Button(tab4, text="Salvar dados", command=save_data)
save_button.pack(pady=12)

status_label = ttk.Label(tab4, text="", foreground="black")
status_label.pack()

tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Rotinas SQL")

title_label_tab5 = ttk.Label(tab5, text="Rotinas SQL", font=("Helvetica", 12, "bold"))
title_label_tab5.pack(pady=5)

days_label = ttk.Label(tab5, text="Selecione os dias:")
days_label.pack(pady=1)

day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
day_labels.append("Lunch")
selectedsql_day_var = tk.StringVar()

def select_daysql(day, button):
    selectedsql_days = selectedsql_day_var.get().split(",")

    if day in selectedsql_days:
        selectedsql_days.remove(day)
        translated_day = day_translation[day]
        button.config(text=f"{translated_day} ☐")
    else:
        selectedsql_days.append(day)
        translated_day = day_translation[day]
        button.config(text=f"{translated_day} ☑")

    selectedsql_day_var.set(",".join(selectedsql_days))

day_buttons_frame = ttk.Frame(tab5)
day_buttons_frame.pack(padx=15, pady=2)

day_buttons = []

for i in range(8):
    row = i // 2
    col = i % 2

    translated_day = day_translation[day_labels[i]]
    day_button_text = f"{translated_day} ☐ "
    day_button = ttk.Button(day_buttons_frame, text=day_button_text)
    day_button.grid(row=row, column=col, padx=5, pady=5)
    day_buttons.append(day_button)

    day_label = day_labels[i]
    translated_day_label = day_translation[day_label]
    day_button.config(command=functools.partial(select_daysql, day_label, day_button))

hour_label = ttk.Label(tab5, text="Hora:")
hour_label.pack()

hour_varsql = tk.StringVar(value="16:30") 
hour_entry = ttk.Entry(tab5, textvariable=hour_var)
hour_entry.pack()

lunch_hour_label = ttk.Label(tab5, text="Horário do Almoço:")
lunch_hour_label.pack()

lunch_varsql = tk.StringVar(value="12:00") 
lunch_hour_entry = ttk.Entry(tab5, textvariable=lunch_var)
lunch_hour_entry.pack()

bat_files = {
    "Lunch": "C:\BKP_1.2\ScriptsSQL\BKPAlmoco.bat",
    "Sun": "C:\BKP_1.2\ScriptsSQL\BKPDomingo.bat",
    "Mon": "C:\BKP_1.2\ScriptsSQL\BKPSegunda.bat",
    "Tue": "C:\BKP_1.2\ScriptsSQL\BKPTerca.bat",
    "Wed": "C:\BKP_1.2\ScriptsSQL\BKPQuarta.bat",
    "Thu": "C:\BKP_1.2\ScriptsSQL\BKPQuinta.bat",
    "Fri": "C:\BKP_1.2\ScriptsSQL\BKPSexta.bat",
    "Sat": "C:\BKP_1.2\ScriptsSQL\BKPSabado.bat",
}

def create_sqltask():
    selected_days = selectedsql_day_var.get().split(",")
    selected_hour = hour_var.get()

    for selected_day in selected_days:
        if selected_day in bat_files:
            batch_file_path = bat_files[selected_day]
            translated_day = day_translation[selected_day]
            task_name = f"SQL {translated_day}"
            task_command = [
                "schtasks", "/create", "/tn", task_name, "/tr", batch_file_path,
                "/sc", "weekly", "/d", selected_day, "/st", selected_hour, "/f",
                "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
            ]

            if selected_day == "Lunch":
                lunch_hour = lunch_hour_entry.get()
                lunch_task_name = f"SQL {translated_day}"
                lunch_task_command = [
                    "schtasks", "/create", "/tn", lunch_task_name, "/tr", batch_file_path,
                    "/sc", "daily", "/st", lunch_hour_entry.get(), "/f",
                    "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
                ]
                subprocess.run(lunch_task_command, capture_output=True, text=True)

            else:
                subprocess.run(task_command, capture_output=True, text=True)

            status_label_tab5.config(text="Rotinas SQL criadas!", foreground="blue")
        else:
            status_label_tab5.config(text=f"Nenhum dia selecionado!", foreground="red")

create_buttons_frame = ttk.Frame(tab5)
create_buttons_frame.pack(padx=15, pady=2)

create_task_button = ttk.Button(create_buttons_frame, text="Criar tarefas", command=create_sqltask)
create_task_button.grid(row=0, column=0, padx=10, pady=5)

def create_startupsql_routine():
    batch_file_path = "C:\BKP_1.2\ScriptsSQL\BackupVerif.exe"
    task_name = "SQL Verifica"
    task_command = [
        "schtasks", "/create", "/tn", task_name, "/tr", batch_file_path,
        "/sc", "onstart", "/f", "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
    ]
    subprocess.run(task_command, capture_output=True, text=True)
    status_label_tab5.config(text="Rotina de verificação criada!", foreground="blue")
    
create_startup_routinesql_button = ttk.Button(create_buttons_frame, text="Rotina de verificação", command=create_startupsql_routine)
create_startup_routinesql_button.grid(row=0, column=1, padx=10, pady=5)

status_label_tab5 = ttk.Label(tab5, text="", foreground="black")
status_label_tab5.pack()

app.mainloop()

# Comando para compilação do executável
"""
pyinstaller --onefile --icon=bin/12.ico --noconsole --add-data "ScriptsSQL;ScriptsSQL"--add-data "ScriptsMySQL;ScriptsMySQL" --add-data "bin;bin" BackupGer.py
"""