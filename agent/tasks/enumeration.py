import subprocess


def do_systeminfo():
    result = subprocess.run("systeminfo", shell=True, capture_output=True)
    return result.stdout
