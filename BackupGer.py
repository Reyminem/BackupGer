import tkinter as tk
from tkinter import ttk
import configparser
import subprocess
import functools
import os
import shutil
import sys

app = tk.Tk()
app.title("BackupGer")
app.geometry("400x360")
icon_path = os.path.join(os.path.dirname(__file__), "12.ico")
app.iconbitmap(icon_path)

# Aplica o tema "clam"
style = ttk.Style()
style.theme_use("clam")

# Widget para criação de um app com várias abas
notebook = ttk.Notebook(app)
notebook.pack(pady=0, fill='both', expand=True)

# Tab 1: Diretórios
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="MySQL")

# Título da primeira aba
title_label_tab1 = ttk.Label(tab1, text="Criação de Diretórios MySQL", font=("Helvetica", 12, "bold"))
title_label_tab1.pack(pady=5)

def create_directories():
    directories_to_create = [
        "C:\\BKP_1.2\\Scripts",
        "C:\\BKP_1.2\\Backup\\Domingo",
        "C:\\BKP_1.2\\Backup\\Segunda", "C:\\BKP_1.2\\Backup\\Terca",
        "C:\\BKP_1.2\\Backup\\Quarta", "C:\\BKP_1.2\\Backup\\Quinta",
        "C:\\BKP_1.2\\Backup\\Sexta", "C:\\BKP_1.2\\Backup\\Sabado",
        "C:\\BKP_1.2\\7-Zip",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Domingo",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Segunda", "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Terca",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Quarta", "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Quinta",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Sexta", "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Sabado"
    ]

    for directory in directories_to_create:
        os.makedirs(directory, exist_ok=True)

    # Copia os arquivos da pasta "Scripts" para "C:\BKP_1.2\Scripts"
    script_target_dir = "C:\\BKP_1.2\\Scripts"
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

    # Obtém o caminho da pasta temporária onde os arquivos foram extraídos
    temp_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    
    # Copia os executáveis do 7-Zip para a pasta temporária
    seven_zip_dir = os.path.join(temp_dir, "C:\\BKP_1.2\\7-Zip")
    if not os.path.exists(seven_zip_dir):
        os.makedirs(seven_zip_dir)

    shutil.copy2(os.path.join(temp_dir, "7z.exe"), seven_zip_dir)
    shutil.copy2(os.path.join(temp_dir, "7z-x64.exe"), seven_zip_dir)

    status_label_tab1.config(text="Diretórios e arquivos criados com sucesso!", foreground="green")

create_directories_button = ttk.Button(tab1, text="Criar diretórios", command=create_directories)
create_directories_button.pack(pady=10)

title_label_tab1 = ttk.Label(tab1, text="Obter a Razão Social do Cliente", font=("Helvetica", 12, "bold"))
title_label_tab1.pack(pady=5)

# Extrai as informações do banco de dados do cliente (Razão social, nome fantasia, CNPJ, etc..)
def execute_bat_script():
    script_name = "MySQLExtract.bat"
    script_path = os.path.join(sys._MEIPASS, script_name) if hasattr(sys, "_MEIPASS") else script_name
    
    try:
        subprocess.run([script_path], shell=True, check=True)
        status_label_tab1.config(text="Dados extraídos com sucesso!", foreground="green")
    except subprocess.CalledProcessError as e:
        status_label_tab1.config(text=f"Erro ao extrair dados: {e}", foreground="red")

execute_button = ttk.Button(tab1, text="Obter dados", command=execute_bat_script)
execute_button.pack(pady=10)

status_label_tab1 = ttk.Label(tab1, text="", foreground="black")
status_label_tab1.pack()

# Tab 2: Diretórios SQL
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="SQL")

# Título da segunda aba
title_label_tab2 = ttk.Label(tab2, text="Criação de Diretórios SQL", font=("Helvetica", 12, "bold"))
title_label_tab2.pack(pady=5)

def create_directories():
    directories_to_create = [
        "C:\\BKP_1.2\\Scripts",
        "C:\\BKP_1.2\\Backup\\Domingo",
        "C:\\BKP_1.2\\Backup\\Segunda", "C:\\BKP_1.2\\Backup\\Terca",
        "C:\\BKP_1.2\\Backup\\Quarta", "C:\\BKP_1.2\\Backup\\Quinta",
        "C:\\BKP_1.2\\Backup\\Sexta", "C:\\BKP_1.2\\Backup\\Sabado",
        "C:\\BKP_1.2\\7-Zip",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Domingo",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Segunda", "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Terca",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Quarta", "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Quinta",
        "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Sexta", "C:\\Program Files (x86)\\12informatica\\BackupDrive\\Sabado"
    ]

    for directory in directories_to_create:
        os.makedirs(directory, exist_ok=True)

    # Copia os arquivos da pasta "Scripts" para "C:\BKP_1.2\Scripts"
    script_target_dir = "C:\\BKP_1.2\\Scripts"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_source_dir = os.path.join(script_dir, "ScriptsSQL")

    for item in os.listdir(scripts_source_dir):
        source_item = os.path.join(scripts_source_dir, item)
        target_item = os.path.join(script_target_dir, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, target_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, target_item)

    # Obtém o caminho da pasta temporária onde os arquivos foram extraídos
    temp_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    
    # Copia os executáveis do 7-Zip para a pasta temporária
    seven_zip_dir = os.path.join(temp_dir, "C:\\BKP_1.2\\7-Zip")
    if not os.path.exists(seven_zip_dir):
        os.makedirs(seven_zip_dir)

    shutil.copy2(os.path.join(temp_dir, "7z.exe"), seven_zip_dir)
    shutil.copy2(os.path.join(temp_dir, "7z-x64.exe"), seven_zip_dir)

    status_label.config(text="Diretórios e arquivos criados com sucesso!", foreground="green")

create_directories_button = ttk.Button(tab2, text="Criar Diretórios", command=create_directories)
create_directories_button.pack(pady=10)

# Função para salvar dados do servidor SQL
def save_data():
    if not (server_name_entry.get() and user_entry.get() and password_entry.get()):
        status_label.config(text="Erro: Preencha todos os campos!", foreground="red")
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

    save_directory = "C:\BKP_1.2\Scripts"
    os.makedirs(save_directory, exist_ok=True)
    
    file_path = os.path.join(save_directory, 'server.ini')
    
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    status_label.config(text="Salvo com sucesso!", foreground="green")

# Títulos para as caixas de entrada
server_name_label = ttk.Label(tab2, text="Servidor:")
server_name_label.pack(pady=2)
server_name_entry = ttk.Entry(tab2)
server_name_entry.pack(pady=2)

user_label = ttk.Label(tab2, text="Usuário:")
user_label.pack(pady=2)
user_entry = ttk.Entry(tab2)
user_entry.pack(pady=2)

password_label = ttk.Label(tab2, text="Senha:")
password_label.pack(pady=2)
password_entry = ttk.Entry(tab2, show='*')
password_entry.pack(pady=2)

save_button = ttk.Button(tab2, text="Salvar dados", command=save_data)
save_button.pack(pady=12)

status_label = ttk.Label(tab2, text="", foreground="black")
status_label.pack()

# Tab 4: criação de rotinas
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Rotinas")

# Título da quarta aba
title_label_tab4 = ttk.Label(tab4, text="Rotinas", font=("Helvetica", 12, "bold"))
title_label_tab4.pack(pady=5)

# Caixas de seleção para os dias
days_label = ttk.Label(tab4, text="Selecione os dias:")
days_label.pack(pady=1)

# Valor padrão para a entrada do horário
hour_var = tk.StringVar(value="16:30")

# Traduz os dias para português
day_translation = {
    "Sun": "Dom",
    "Mon": "Seg",
    "Tue": "Ter",
    "Wed": "Qua",
    "Thu": "Qui",
    "Fri": "Sex",
    "Sat": "Sáb",
}

day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
selected_day_var = tk.StringVar()

# Função para a seleção dos dias
def select_day(day, button):
    selected_days = selected_day_var.get().split(",")

    if day in selected_days:
        selected_days.remove(day)
        translated_day = day_translation[day]
        button.config(text=f"{translated_day} ☐")
    else:
        selected_days.append(day)
        translated_day = day_translation[day]
        button.config(text=f"{translated_day} ☑")

    selected_day_var.set(",".join(selected_days))

# Frame para os botões na aba 3
day_buttons_frame = ttk.Frame(tab4)
day_buttons_frame.pack(padx=15, pady=2)

# Loop para a criação dos botões
day_buttons = []

for i in range(7):
    row = i // 2
    col = i % 2

    translated_day = day_translation[day_labels[i]]
    day_button_text = f"{translated_day} ☐ "
    day_button = ttk.Button(day_buttons_frame, text=day_button_text)
    day_button.grid(row=row, column=col, padx=5, pady=5)
    day_buttons.append(day_button)

    day_label = day_labels[i]
    translated_day_label = day_translation[day_label]
    day_button.config(command=functools.partial(select_day, day_label, day_button))

# Caixa para a entrada do horário
hour_label = ttk.Label(tab4, text="Hora:")
hour_label.pack()

hour_entry = ttk.Entry(tab4, textvariable=hour_var)
hour_entry.pack()

bat_files = {
    "Sun": "C:\BKP_1.2\Scripts\BKPDomingo.bat",
    "Mon": "C:\BKP_1.2\Scripts\BKPSegunda.bat",
    "Tue": "C:\BKP_1.2\Scripts\BKPTerca.bat",
    "Wed": "C:\BKP_1.2\Scripts\BKPQuarta.bat",
    "Thu": "C:\BKP_1.2\Scripts\BKPQuinta.bat",
    "Fri": "C:\BKP_1.2\Scripts\BKPSexta.bat",
    "Sat": "C:\BKP_1.2\Scripts\BKPSabado.bat",
}

# Função para a criação das tarefas no agendador
def create_task():
    selected_days = selected_day_var.get().split(",")
    selected_hour = hour_var.get()

    for selected_day in selected_days:
        if selected_day in bat_files:
            batch_file_path = bat_files[selected_day]
            translated_day = day_translation[selected_day]
            task_name = f"BKP {translated_day}"
            task_command = [
                "schtasks", "/create", "/tn", task_name, "/tr", batch_file_path,
                "/sc", "weekly", "/d", selected_day, "/st", selected_hour, "/f",
                "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
            ]
            subprocess.run(task_command, capture_output=True, text=True)
            status_label_tab4.config(text="Tarefas criadas!", foreground="blue")
        else:
            status_label_tab4.config(text=f"Nenhum dia selecionado!", foreground="red")

# Botão para a criação da rotina de inicialização do computador
def create_startup_routine():
    batch_file_path = "C:\BKP_1.2\Scripts\ScanData.bat"
    task_name = "BKP E-mail"
    task_command = [
        "schtasks", "/create", "/tn", task_name, "/tr", batch_file_path,
        "/sc", "onstart", "/f", "/rl", "HIGHEST", "/RU", "NT AUTHORITY\SYSTEM", "/IT"
    ]
    subprocess.run(task_command, capture_output=True, text=True)
    status_label_tab4.config(text="Rotina de e-mail criada!", foreground="blue")

# Frame para os botões de criação de rotina
create_buttons_frame = ttk.Frame(tab4)
create_buttons_frame.pack(padx=15, pady=2)

# Botão para criar tarefas
create_task_button = ttk.Button(create_buttons_frame, text="Criar tarefas", command=create_task)
create_task_button.grid(row=0, column=0, padx=10, pady=10)

# Botão para criar a rotina de inicialização do computador
create_startup_routine_button = ttk.Button(create_buttons_frame, text="Criar rotina de E-mail", command=create_startup_routine)
create_startup_routine_button.grid(row=0, column=1, padx=10, pady=10)

status_label_tab4 = ttk.Label(tab4, text="", foreground="black")
status_label_tab4.pack()

# Tab 5: Versão do Programa
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Sobre")

version_label_tab5 = ttk.Label(tab5, text="Versão do Programa: 4.0.2", font=("Helvetica", 12, "bold"), justify="center")
version_label_tab5.pack(pady=20)
version_label_tab5 = ttk.Label(tab5, text="Programa voltado para a configuração de rotinas\n de backup automáticas do MySQL e SQL Server.", justify="center")
version_label_tab5.pack(pady=20)
version_label_tab5 = ttk.Label(tab5, text="Desenvolvido por Reynaldo. Compilado no dia 30/08/2023.", justify="center")
version_label_tab5.pack(pady=20)

app.mainloop()

# Comando para compilação do executável
"""
pyinstaller --onefile --icon=12.ico --noconsole --add-data "ScriptsSQL;ScriptsSQL" --add-data "ScriptsMySQL;ScriptsMySQL"
--add-data "7z.exe;." --add-data "7z-x64.exe;." --add-data "MySQLExtract.bat;." --add-data "12.ico;." BackupGer.py
"""