import subprocess
import sys
import shlex

def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    sanitized_command = shlex.quote(command)
    sanitized_args = [shlex.quote(arg) for arg in args]

    completed_process = subprocess.run([sanitized_command, *sanitized_args], capture_output=True)
    print(completed_process.stdout.decode("utf-8"))

if __name__ == "__main__":
    main()
