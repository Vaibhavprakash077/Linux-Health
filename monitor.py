# Linux Health Monitor - Feature Version
import argparse
import system_checks as s

parser = argparse.ArgumentParser()

parser.add_argument("--memory", action="store_true")
parser.add_argument("--disk", action="store_true")
parser.add_argument("--hostname", action="store_true")
parser.add_argument("--user", action="store_true")
parser.add_argument("--service")
parser.add_argument("--all", action="store_true")

args = parser.parse_args()

if args.memory:
    s.check_memory()

if args.disk:
    s.check_disk()

if args.hostname:
    s.check_hostname()

if args.user:
    s.check_current_user()

if args.service:
    s.check_service(args.service)

if args.all:
    s.check_current_user()
    s.check_disk()
    s.check_hostname()
    s.check_memory()

    if args.service:
        s.check_service(args.service)