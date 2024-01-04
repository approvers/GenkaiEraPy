import io
import subprocess
import sys
import threading
from typing import Callable

from load_env import load_dotenv


class CommandError(RuntimeError):
    pass


def stream_reader(stream: io.TextIOBase, callback: Callable[[str], None]) -> None:
    while True:
        line = stream.readline()

        if line:
            callback(line.strip())

        else:
            break


def execute_command(command_list: list[str]) -> None:
    print("Executing command:", " ".join(command_list))

    with subprocess.Popen(
        command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    ) as proc:
        # Start threads to read the stdout and stderr streams
        stdout_thread = threading.Thread(
            target=stream_reader, args=(proc.stdout, print)
        )
        stderr_thread = threading.Thread(
            target=stream_reader, args=(proc.stderr, print)
        )

        stdout_thread.start()
        stderr_thread.start()

        stdout_thread.join()
        stderr_thread.join()

    if (proc.returncode is None) or (proc.returncode != 0):
        raise CommandError(
            f"Error in command execution with return code: {proc.returncode}"
        )


def main() -> None:
    command_list = sys.argv[1:]

    load_dotenv()

    execute_command(command_list)


if __name__ == "__main__":
    main()
