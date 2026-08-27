# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TaskPulse
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="TaskPulse CLI")
    sub = parser.add_subparsers(dest="command")
    p = sub.add_parser("list", help="list tasks")
    p = sub.add_parser("add", help="add task")
    p = sub.add_parser("done", help="mark done")
    p = sub.add_parser("journal", help="daily log")
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    print(f"[TaskPulse] command={args.command}")
