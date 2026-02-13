import subprocess

running = {}

def start_bot(file_path):
    try:
        process = subprocess.Popen(
            ["python3", file_path]
        )
        running[file_path] = process
        return True
    except:
        return False