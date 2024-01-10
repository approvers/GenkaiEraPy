import argparse
import os
import subprocess
import time

from load_env import load_dotenv

RUNCOMMAND_PATH = "script/run_command.py"

parser = argparse.ArgumentParser()
parser.add_argument("--online", action="store_true")
parser.add_argument("--max_retries", type=int, default=5)
parser.add_argument("positional_arg", nargs="*")

args = parser.parse_args()
load_dotenv()

if args.online:
    print("Online mode. The `--online` flag is enabled.")
else:
    print("Offline mode. The `--online` flag is disabled.")


USER = "genkaiera_app"
DB = "genkaiera"
PASSWORD = os.environ.get("GENKAIERA_POSTGRES_PASSWORD")
HOST = os.environ.get("GENKAIERA_POSTGRES_HOST")
PORT = os.environ.get("GENKAIERA_POSTGRES_PORT")

max_retries = args.max_retries

for i in range(max_retries):
    try:
        subprocess.check_call(
            [
                "python",
                RUNCOMMAND_PATH,
                "psql",
                f"user={USER} password={PASSWORD} host={HOST} port={PORT} dbname={DB}",
                "-c",
                r"\q",
            ]
        )
        print("DB is ready!")
        break
    except subprocess.CalledProcessError:
        if i < max_retries:
            print(
                f"DB is not ready yet. Waiting for 5 seconds...  (Retry: {i}/{max_retries})"
            )
            time.sleep(5)
        else:
            print("DB is unavailable after maximum retries. Exiting...")
            exit(1)

target_dbs = [f"{DB}_test", DB]

for target_db in target_dbs:
    print(f"Applying migrations for {target_db}...")
    env = os.environ.copy()
    env["GENKAIERA_POSTGRES_DB_NAME"] = target_db

    if args.online:
        subprocess.check_call(["alembic", "upgrade", "head"], env=env)
    else:
        subprocess.check_call(["alembic", "upgrade", "head", "--sql"], env=env)

    print(f"Migrations applied for {target_db}!")
