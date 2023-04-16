import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, shell=True)
        return result.stdout
    except Exception as e:
        return str(e)