import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import configparser
import subprocess
import functools
import os
import shutil
import tempfile
import winshell

# Personalização do programa e da janela
app = ThemedTk(theme="breeze")
app.title("BackupGer")
app.geometry("460x470")
icon_path = os.path.join(os.path.dirname(__file__), "bin", "12.ico")
app.iconbitmap(icon_path)

# Widget para criação de um app com várias abas
notebook = ttk.Notebook(app)
notebook.pack(pady=0, fill='both', expand=True)

# Aba de configurações
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Config")

# Frame para gravar o ID
frame1_tab1 = ttk.Frame(tab1)
frame1_tab1.pack(pady=30)

# Função para salvar o ID do cliente
def save_id():
    if not (id_entry.get()):
        message_label.config(text="Erro: preencha o ID!", foreground="red")
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
    message_label.config(text="Salvo com sucesso!", foreground="green")

title_label_tab1 = ttk.Label(frame1_tab1, text="ID do Cliente", takefocus=True, font=("Helvetica", 12, "bold"))
title_label_tab1.pack(pady=10)

id_entry = ttk.Entry(frame1_tab1)
id_entry.pack(pady=2)

save_button = ttk.Button(frame1_tab1, text="Salvar ID", takefocus=False, command=save_id)
save_button.pack(pady=10)

message_label = ttk.Label(frame1_tab1, text="", foreground="black")
message_label.pack()

# Frame para as funções do 7-Zip
frame2_tab1 = ttk.Frame(tab1)
frame2_tab1.pack(padx=15, pady=20)

title_label_tab1 = ttk.Label(frame2_tab1, text="Instalar 7-Zip", font=("Helvetica", 12, "bold"))
title_label_tab1.grid(row=0, column=0, columnspan=2, pady=10)

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
        
def executar_7z_x64():
    try:
        temp_dir = tempfile.mkdtemp()
        
        shutil.copy2(os.path.join(seven_zip_dir, "7z-x64.exe"), temp_dir)

        subprocess.run([os.path.join(temp_dir, "7z-x64.exe")])

        shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Erro ao executar 7z-x64.exe: {e}")

title_label_tab1 = ttk.Label(frame2_tab1, text="Instalar 7-Zip", font=("Helvetica", 12, "bold"))
title_label_tab1.grid(row=0, column=0, columnspan=2, pady=10)

# Botão para instalação do 7-Zip 32 bits
button_7z = ttk.Button(frame2_tab1, text="32 Bits", takefocus=False, command=executar_7z)
button_7z.grid(row=1, column=0, padx=10, pady=5)

# Botão para instalação do 7-Zip 64 bits
button_7z_x64 = ttk.Button(frame2_tab1, text="64 Bits", takefocus=False, command=executar_7z_x64)
button_7z_x64.grid(row=1, column=1, padx=10, pady=5)

status_label_tab1 = ttk.Label(tab1, text="", foreground="black")
status_label_tab1.pack()

# Aba de diretórios MySQL
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="MySQL")

frame_tab2 = ttk.Frame(tab2)
frame_tab2.pack(pady=25)

# Título
title_label_tab2 = ttk.Label(frame_tab2, text="Criação de Diretórios MySQL", font=("Helvetica", 12, "bold"))
title_label_tab2.pack(pady=5)

# Função para criação dos diretórios
def create_directories():
    base_path = "C:\\BKP_1.2"
    subdirectories = ["ScriptsMySQL", "Backup\\Domingo", "Backup\\Almoco", "Backup\\Segunda", "Backup\\Terca",
                      "Backup\\Quarta", "Backup\\Quinta", "Backup\\Sexta", "Backup\\Sabado", "Backup\\Desligar"]

    for directory in subdirectories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    base_path_2 = "C:\\Program Files (x86)\\12informatica\\BackupDrive"
    subdirectories_2 = ["Domingo", "Almoco", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Desligar"]

    for directory in subdirectories_2:
        os.makedirs(os.path.join(base_path_2, directory), exist_ok=True)

    # Copia os arquivos da pasta "Scripts" para "C:\BKP_1.2\Scripts"
    script_target_dir = "C:\\BKP_1.2\\ScriptsMySQL"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_source_dir = os.path.join(script_dir, "ScriptsMySQL")

    for item in os.listdir(scripts_source_dir):
        if item == "BKPDesligar.bat":
                continue

        source_item = os.path.join(scripts_source_dir, item)
        target_item = os.path.join(script_target_dir, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, target_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, target_item)

    source_exe = os.path.join(script_dir, "bin", "BackupVerif.exe")
    target_exe = os.path.join(script_target_dir, "BackupVerif.exe")
    shutil.copy(source_exe, target_exe)

    status_label_tab2.config(text="Diretórios e arquivos criados com sucesso!", foreground="green")

create_directories_button = ttk.Button(frame_tab2, text="Criar diretórios", takefocus=False, command=create_directories)
create_directories_button.pack(pady=10)

status_label_tab2 = ttk.Label(frame_tab2, text="", foreground="black")
status_label_tab2.pack()

frame2_tab2 = ttk.Frame(tab2)
frame2_tab2.pack(pady=1)

# Título
title_label_tab2 = ttk.Label(frame2_tab2, text="Backup ao Desligar", font=("Helvetica", 12, "bold"))
title_label_tab2.pack(pady=5)

def mysql_shutdown():
    base_path = "C:\\BKP_1.2"
    subdirectories = ["Backup\\Desligar"]

    for directory in subdirectories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    base_path_2 = "C:\\Program Files (x86)\\12informatica\\BackupDrive"
    subdirectories_2 = ["Desligar"]

    for directory in subdirectories_2:
        os.makedirs(os.path.join(base_path_2, directory), exist_ok=True)

    # Copia os arquivos da pasta "ScriptsMySQL" para "C:\BKP_1.2\ScriptsMySQL"
    script_target_dir = "C:\\BKP_1.2\\ScriptsMySQL"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_source_path = os.path.join(script_dir, "ScriptsMySQL", "BKPDesligar.bat")
    script_target_path = os.path.join(script_target_dir, "BKPDesligar.bat")
    source_exe = os.path.join(script_dir, "bin", "BackupVerif.exe")
    target_exe = os.path.join(script_target_dir, "BackupVerif.exe")

    try:
        shutil.copy2(script_source_path, script_target_path)
        shutil.copy2(source_exe, target_exe)

        desktop = winshell.desktop()
        path = os.path.join(desktop, "Desligar.lnk")
        target = r"C:\BKP_1.2\ScriptsMySQL\BKPDesligar.BAT"
        
        shortcut = winshell.shortcut(path)
        shortcut.path = target
        shortcut.icon_location = (r"%SystemRoot%\system32\SHELL32.dll", 27)  # Ícone de desligamento do Windows
        shortcut.write()
        
        frame2_tab2_status_label.config(text="Atalho criado com sucesso!", foreground="green")
    except Exception as e:
        frame2_tab2_status_label.config(text=f"Erro ao criar atalho: {str(e)}", foreground="red")

# Botão para criar o atalho
mysql_shutdown_button = ttk.Button(frame2_tab2, text="Criar atalho", command=mysql_shutdown)
mysql_shutdown_button.pack(pady=10)

frame2_tab2_status_label = ttk.Label(frame2_tab2, text="", foreground="black")
frame2_tab2_status_label.pack()

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
    "Sun": "Domingo",
    "Mon": "Segunda",
    "Tue": "Terça",
    "Wed": "Quarta",
    "Thu": "Quinta",
    "Fri": "Sexta",
    "Sat": "Sábado",
    "Lunch": "Almoço",
}

# Legenda para os botões dos dias
day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
day_labels.append("Lunch")
selectedmysql_day_var = tk.StringVar()

# Função para a seleção dos dias
def select_daymysql(day, checkbutton_var):
    selectedmysql_days = selectedmysql_day_var.get().split(",")

    if day in selectedmysql_days:
        selectedmysql_days.remove(day)
        translated_day = day_translation[day]
        checkbutton_var.set(0)  # Desmarcar a caixa de seleção
    else:
        selectedmysql_days.append(day)
        translated_day = day_translation[day]
        checkbutton_var.set(1)  # Marcar a caixa de seleção

    selectedmysql_day_var.set(",".join(selectedmysql_days))

day_buttons_frame = ttk.Frame(tab3)
day_buttons_frame.pack(padx=20, pady=10)

# Configurar colunas da grade para ter o mesmo tamanho
day_buttons_frame.grid_columnconfigure(0, weight=1)
day_buttons_frame.grid_columnconfigure(1, weight=1)

day_checkbuttons = []

for i in range(8):
    row = i // 3
    col = i % 3

    translated_day = day_translation[day_labels[i]]
    day_checkbutton_var = tk.IntVar()  # Variável para controlar o estado da caixa de seleção
    day_checkbutton = ttk.Checkbutton(day_buttons_frame, text=translated_day, variable=day_checkbutton_var)
    day_checkbutton.grid(row=row, column=col, padx=5, pady=5, sticky="w")  # Usar "w" para alinhar à esquerda
    day_checkbuttons.append(day_checkbutton)

    day_label = day_labels[i]
    day_checkbutton.config(command=functools.partial(select_daymysql, day_label, day_checkbutton_var))

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

            status_label_tab3.config(text="Rotinas MySQL criadas!", foreground="green")
        else:
            status_label_tab3.config(text=f"Nenhum dia selecionado!", foreground="red")

# Função para a criação da rotina de scan para verificação
def create_startup_routine():
    batch_file_path = r"C:\BKP_1.2\ScriptsMySQL\BackupVerif.exe"  # Usa 'r' antes da string para evitar problemas com barras invertidas
    task_name = "MySQL Verifica"
    
    # Usa o diretório C:\BKP_1.2 como diretório temporário
    temp_dir = r"C:\BKP_1.2"

    # Define o caminho completo para o arquivo XML dentro do diretório temporário
    xml_file_path = os.path.join(temp_dir, "tarefa.xml")

    # Define o conteúdo XML da tarefa agendada
    xml_content = f"""
    <Task version="1.6" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
        <Triggers>
            <LogonTrigger>
                <ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
                <Enabled>true</Enabled>
                <Delay>PT1M</Delay>
            </LogonTrigger>
        </Triggers>
        <Principals>
            <Principal id="Author">
            <UserId>NT AUTHORITY\\SYSTEM</UserId>
            <RunLevel>HighestAvailable</RunLevel>
            </Principal>
        </Principals>
        <Settings>
            <MultipleInstancesPolicy>StopExisting</MultipleInstancesPolicy>
            <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
            <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
            <AllowHardTerminate>true</AllowHardTerminate>
            <StartWhenAvailable>false</StartWhenAvailable>
            <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
            <IdleSettings>
            <StopOnIdleEnd>true</StopOnIdleEnd>
            <RestartOnIdle>false</RestartOnIdle>
            </IdleSettings>
            <AllowStartOnDemand>true</AllowStartOnDemand>
            <Enabled>true</Enabled>
            <Hidden>false</Hidden>
            <RunOnlyIfIdle>false</RunOnlyIfIdle>
            <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
            <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
            <WakeToRun>false</WakeToRun>
            <ExecutionTimeLimit>PT1H</ExecutionTimeLimit>
            <Priority>7</Priority>
        </Settings>
        <Actions Context="Author">
            <Exec>
                <Command>{batch_file_path}</Command>
            </Exec>
            <Exec>
                <Command>timeout</Command>
                <Arguments>60</Arguments>
            </Exec>
            <Exec>
                <Command>{batch_file_path}</Command>
            </Exec>
            <Exec>
                <Command>timeout</Command>
                <Arguments>60</Arguments>
            </Exec>
            <Exec>
                <Command>{batch_file_path}</Command>
            </Exec>
        </Actions>
        </Task>

    """

    # Salva o conteúdo XML no arquivo dentro do diretório temporário
    with open(xml_file_path, "w") as xml_file:
        xml_file.write(xml_content)

    # Cria a tarefa agendada usando o comando schtasks
    task_command = [
        "schtasks", "/create", "/tn", task_name, "/xml", xml_file_path, "/F"
    ]

    try:
        subprocess.run(task_command, capture_output=True, text=True, check=True)
        status_label_tab3.config(text="Rotina de verificação criada!", foreground="blue")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar a tarefa agendada: {e}")
    finally:
        # Exclua apenas o arquivo XML temporário
        os.remove(xml_file_path)    

def replace_mysql_line_shutdown(script_path):
    try:
        with open(script_path, 'r') as script_file:
            lines = script_file.readlines()

        if lines:
            lines[-1] = "shutdown -s -t 15"

        with open(script_path, 'w') as script_file:
            script_file.writelines(lines)

        status_label_tab3.config(text="Alterado com sucesso!", foreground="green")
    except Exception as e:
        status_label_tab3.config(text=f"Erro ao alterar scripts: {str(e)}", foreground="red")  

def shutdown_mysql_scripts():
    scripts_directory = "C:\\BKP_1.2\\ScriptsMySQL"
    
    # Verificar se o diretório existe
    if os.path.exists(scripts_directory):
        for root, _, files in os.walk(scripts_directory):
            for filename in files:
                if filename.endswith(".bat"):
                    script_path = os.path.join(root, filename)
                    replace_mysql_line_shutdown(script_path)

# Frame para os botões de criação de rotina
create_buttons_frame = ttk.Frame(tab3)
create_buttons_frame.pack(padx=15, pady=15)

# Botão para criar tarefas
create_mysqltask_button = ttk.Button(create_buttons_frame, text="Criar tarefas", command=create_mysqltask)
create_mysqltask_button.grid(row=0, column=0, padx=10, pady=5)

# Botão para criar a rotina de verificação
create_startup_routine_button = ttk.Button(create_buttons_frame, text="Rotina de verificação", command=create_startup_routine)
create_startup_routine_button.grid(row=0, column=1, padx=10, pady=5)

# Botão para adicionar shutdown aos scripts
shutdown_button = ttk.Button(create_buttons_frame, text="Desligar após execução", command=shutdown_mysql_scripts)
shutdown_button.grid(row=1, column=0, columnspan=2, padx=10, pady=7, sticky="n")

status_label_tab3 = ttk.Label(tab3, text="", foreground="black")
status_label_tab3.pack()

# Diretórios SQL
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="SQL")

frame1_tab4 = ttk.Frame(tab4)
frame1_tab4.pack(pady=10)

title_label_tab4 = ttk.Label(frame1_tab4, text="Criação de Diretórios SQL", font=("Helvetica", 12, "bold"))
title_label_tab4.pack(pady=5)

def create_directories():
    base_path = "C:\\BKP_1.2"
    subdirectories = ["ScriptsSQL", "Backup\\Domingo", "Backup\\Almoco", "Backup\\Segunda", "Backup\\Terca",
                      "Backup\\Quarta", "Backup\\Quinta", "Backup\\Sexta", "Backup\\Sabado", "Backup\\Desligar"]

    for directory in subdirectories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    base_path_2 = "C:\\Program Files (x86)\\12informatica\\BackupDrive"
    subdirectories_2 = ["Domingo", "Almoco", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Desligar"]

    for directory in subdirectories_2:
        os.makedirs(os.path.join(base_path_2, directory), exist_ok=True)

    script_target_dir = "C:\\BKP_1.2\\ScriptsSQL"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_source_dir = os.path.join(script_dir, "ScriptsSQL")

    try:
        for item in os.listdir(scripts_source_dir):
            if item == "BKPDesligar.bat":
                continue

            source_item = os.path.join(scripts_source_dir, item)
            target_item = os.path.join(script_target_dir, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, target_item)

        source_exe = os.path.join(script_dir, "bin", "BackupVerif.exe")
        target_exe = os.path.join(script_target_dir, "BackupVerif.exe")
        shutil.copy(source_exe, target_exe)

        frame1_tab4_status_label.config(text="Diretórios e arquivos criados com sucesso!", foreground="green")
    except Exception as e:
    
        frame1_tab4_status_label.config(text=f"Erro: {str(e)}", foreground="red")         

create_directories_button = ttk.Button(frame1_tab4, text="Criar diretórios", command=create_directories)
create_directories_button.pack(pady=5)

frame1_tab4_status_label = ttk.Label(frame1_tab4, text="", foreground="black")
frame1_tab4_status_label.pack()

frame2_tab4 = ttk.Frame(tab4)
frame2_tab4.pack(pady=0)

title_label_tab4 = ttk.Label(frame2_tab4, text="Informações do Servidor", font=("Helvetica", 12, "bold"))
title_label_tab4.pack(ipady=0)

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

# Subframe para rótulos e entradas do servidor
server_frame = ttk.Frame(frame2_tab4)
server_frame.pack(pady=1)

server_name_label = ttk.Label(server_frame, text="Servidor:")
server_name_entry = ttk.Entry(server_frame)
server_name_label.grid(row=0, column=0, padx=0, pady=3, sticky="e")
server_name_entry.grid(row=0, column=1, padx=0, pady=6, sticky="w")

# Subframe para rótulos e entradas do usuário
user_frame = ttk.Frame(frame2_tab4)
user_frame.pack(pady=1)

user_label = ttk.Label(user_frame, text="Usuário:")
user_entry = ttk.Entry(user_frame)
user_label.grid(row=0, column=0, padx=1, pady=3, sticky="e")
user_entry.grid(row=0, column=1, padx=0, pady=6, sticky="w")

# Subframe para rótulos e entradas da senha
password_frame = ttk.Frame(frame2_tab4)
password_frame.pack(pady=1)

password_label = ttk.Label(password_frame, text="Senha:")
password_entry = ttk.Entry(password_frame, show='*')
password_label.grid(row=0, column=0, padx=4, pady=3, sticky="e")
password_entry.grid(row=0, column=1, padx=1, pady=6, sticky="w")

save_button = ttk.Button(frame2_tab4, text="Salvar dados", command=save_data)
save_button.pack(pady=8)

status_label = ttk.Label(frame2_tab4, text="", foreground="black")
status_label.pack()

frame3_tab4 = ttk.Frame(tab4)
frame3_tab4.pack(pady=1)

# Título
title_label_tab4 = ttk.Label(frame3_tab4, text="Backup ao Desligar", font=("Helvetica", 12, "bold"))
title_label_tab4.pack(pady=5)

def sql_shutdown():

    base_path = "C:\\BKP_1.2"
    subdirectories = ["Backup\\Desligar"]

    for directory in subdirectories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    base_path_2 = "C:\\Program Files (x86)\\12informatica\\BackupDrive"
    subdirectories_2 = ["Desligar"]

    for directory in subdirectories_2:
        os.makedirs(os.path.join(base_path_2, directory), exist_ok=True)

    script_target_dir = "C:\\BKP_1.2\\ScriptsSQL"
    if not os.path.exists(script_target_dir):
        os.makedirs(script_target_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_source_path = os.path.join(script_dir, "ScriptsSQL", "BKPDesligar.bat")
    script_target_path = os.path.join(script_target_dir, "BKPDesligar.bat")
    source_exe = os.path.join(script_dir, "bin", "BackupVerif.exe")
    target_exe = os.path.join(script_target_dir, "BackupVerif.exe")

    try:
        shutil.copy2(script_source_path, script_target_path)
        shutil.copy2(source_exe, target_exe)

        desktop = winshell.desktop()
        path = os.path.join(desktop, "Desligar.lnk")
        target = r"C:\BKP_1.2\ScriptsSQL\BKPDesligar.BAT"
        
        shortcut = winshell.shortcut(path)
        shortcut.path = target
        shortcut.icon_location = (r"%SystemRoot%\system32\SHELL32.dll", 27)  # Ícone de desligamento do Windows
        shortcut.write()
        
        frame3_tab4_status_label.config(text="Atalho criado com sucesso!", foreground="green")
    except Exception as e:
        frame3_tab4_status_label.config(text=f"Erro ao criar atalho: {str(e)}", foreground="red")

sql_shutdown_button = ttk.Button(frame3_tab4, text="Criar atalho", command=sql_shutdown)
sql_shutdown_button.pack(pady=10)

frame3_tab4_status_label = ttk.Label(frame3_tab4, text="", foreground="black")
frame3_tab4_status_label.pack()

tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Rotinas SQL")

title_label_tab5 = ttk.Label(tab5, text="Rotinas SQL", font=("Helvetica", 12, "bold"))
title_label_tab5.pack(pady=5)

days_label = ttk.Label(tab5, text="Selecione os dias:")
days_label.pack(pady=1)

day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
day_labels.append("Lunch")
selectedsql_day_var = tk.StringVar()

def select_daysql(day, checkbutton_var):
    selectedsql_days = selectedsql_day_var.get().split(",")

    if day in selectedsql_days:
        selectedsql_days.remove(day)
        translated_day = day_translation[day]
        checkbutton_var.set(0)  # Desmarcar a caixa de seleção
    else:
        selectedsql_days.append(day)
        translated_day = day_translation[day]
        checkbutton_var.set(1)  # Marcar a caixa de seleção

    selectedsql_day_var.set(",".join(selectedsql_days))

day_buttons_frame = ttk.Frame(tab5)
day_buttons_frame.pack(padx=20, pady=10)

# Configurar colunas da grade para ter o mesmo tamanho
day_buttons_frame.grid_columnconfigure(0, weight=1)
day_buttons_frame.grid_columnconfigure(1, weight=1)

day_checkbuttons = []

for i in range(8):
    row = i // 3
    col = i % 3

    translated_day = day_translation[day_labels[i]]
    day_checkbutton_var = tk.IntVar()  # Variável para controlar o estado da caixa de seleção
    day_checkbutton = ttk.Checkbutton(day_buttons_frame, text=translated_day, variable=day_checkbutton_var)
    day_checkbutton.grid(row=row, column=col, padx=5, pady=5, sticky="w")  # Usar "w" para alinhar à esquerda
    day_checkbuttons.append(day_checkbutton)

    day_label = day_labels[i]
    day_checkbutton.config(command=functools.partial(select_daysql, day_label, day_checkbutton_var))

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

            status_label_tab5.config(text="Rotinas SQL criadas!", foreground="green")
        else:
            status_label_tab5.config(text=f"Nenhum dia selecionado!", foreground="red")

create_buttons_frame = ttk.Frame(tab5)
create_buttons_frame.pack(padx=15, pady=15)

create_task_button = ttk.Button(create_buttons_frame, text="Criar tarefas", command=create_sqltask)
create_task_button.grid(row=0, column=0, padx=10, pady=5)

def create_startupsql_routine():
    batch_file_path = r"C:\BKP_1.2\ScriptsSQL\BackupVerif.exe"  # Usa 'r' antes da string para evitar problemas com barras invertidas
    task_name = "SQL Verifica"
    
    # Usa o diretório C:\BKP_1.2 como diretório temporário
    temp_dir = r"C:\BKP_1.2"

    # Define o caminho completo para o arquivo XML dentro do diretório temporário
    xml_file_path = os.path.join(temp_dir, "tarefa.xml")

    # Define o conteúdo XML da tarefa agendada
    xml_content = f"""
    <Task version="1.6" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
        <Triggers>
            <LogonTrigger>
                <ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
                <Enabled>true</Enabled>
                <Delay>PT1M</Delay>
            </LogonTrigger>
        </Triggers>
        <Principals>
            <Principal id="Author">
            <UserId>NT AUTHORITY\\SYSTEM</UserId>
            <RunLevel>HighestAvailable</RunLevel>
            </Principal>
        </Principals>
        <Settings>
            <MultipleInstancesPolicy>StopExisting</MultipleInstancesPolicy>
            <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
            <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
            <AllowHardTerminate>true</AllowHardTerminate>
            <StartWhenAvailable>false</StartWhenAvailable>
            <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
            <IdleSettings>
            <StopOnIdleEnd>true</StopOnIdleEnd>
            <RestartOnIdle>false</RestartOnIdle>
            </IdleSettings>
            <AllowStartOnDemand>true</AllowStartOnDemand>
            <Enabled>true</Enabled>
            <Hidden>false</Hidden>
            <RunOnlyIfIdle>false</RunOnlyIfIdle>
            <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
            <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
            <WakeToRun>false</WakeToRun>
            <ExecutionTimeLimit>PT1H</ExecutionTimeLimit>
            <Priority>7</Priority>
        </Settings>
        <Actions Context="Author">
            <Exec>
                <Command>{batch_file_path}</Command>
            </Exec>
            <Exec>
                <Command>timeout</Command>
                <Arguments>60</Arguments>
            </Exec>
            <Exec>
                <Command>{batch_file_path}</Command>
            </Exec>
            <Exec>
                <Command>timeout</Command>
                <Arguments>60</Arguments>
            </Exec>
            <Exec>
                <Command>{batch_file_path}</Command>
            </Exec>
        </Actions>
        </Task>

    """

    # Salva o conteúdo XML no arquivo dentro do diretório temporário
    with open(xml_file_path, "w") as xml_file:
        xml_file.write(xml_content)

    # Cria a tarefa agendada usando o comando schtasks
    task_command = [
        "schtasks", "/create", "/tn", task_name, "/xml", xml_file_path, "/F"
    ]

    try:
        subprocess.run(task_command, capture_output=True, text=True, check=True)
        status_label_tab5.config(text="Rotina de verificação criada!", foreground="blue")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar a tarefa agendada: {e}")
    finally:
        # Exclua apenas o arquivo XML temporário
        os.remove(xml_file_path)

def replace_sql_line_shutdown(script_path):
    try:
        with open(script_path, 'r') as script_file:
            lines = script_file.readlines()

        if lines:
            lines[-1] = "shutdown -s -t 15"

        with open(script_path, 'w') as script_file:
            script_file.writelines(lines)

        status_label_tab5.config(text="Alterado com sucesso!", foreground="green")
    except Exception as e:
        status_label_tab5.config(text=f"Erro ao alterar scripts: {str(e)}", foreground="red")

def shutdown_sql_scripts():
    scripts_directory = "C:\\BKP_1.2\\ScriptsSQL"
    
    # Verificar se o diretório existe
    if os.path.exists(scripts_directory):
        for root, _, files in os.walk(scripts_directory):
            for filename in files:
                if filename.endswith(".bat"):
                    script_path = os.path.join(root, filename)
                    replace_sql_line_shutdown(script_path)

create_startup_routinesql_button = ttk.Button(create_buttons_frame, text="Rotina de verificação", command=create_startupsql_routine)
create_startup_routinesql_button.grid(row=0, column=1, padx=10, pady=5)

shutdown_button = ttk.Button(create_buttons_frame, text="Desligar após execução", command=shutdown_sql_scripts)
shutdown_button.grid(row=1, column=0, columnspan=2, padx=10, pady=7, sticky="n")

status_label_tab5 = ttk.Label(tab5, text="", foreground="black")
status_label_tab5.pack()

app.mainloop()

# Anotações úteis
"""
pyinstaller --onefile --icon=bin/12.ico --noconsole --add-data "ScriptsSQL;ScriptsSQL"--add-data "ScriptsMySQL;ScriptsMySQL" --add-data "bin;bin" BackupGer.py
--distpath ~/Desktop BackupGer.py

from ttkthemes import ThemedTk
app = ThemedTk(theme="breeze")
"""