import subprocess


app_commands = [
    "uvicorn add.add:app --host 127.0.0.1 --port 8010",
    "uvicorn subtract.subtract:app --host 127.0.0.1 --port 8020",
    "uvicorn multiply.multiply:app --host 127.0.0.1 --port 8030",
    "uvicorn divide.divide:app --host 127.0.0.1 --port 8040",
]


for cmd in app_commands:
    subprocess.Popen(cmd, shell=True)
