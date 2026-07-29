import subprocess
import logging

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    force=True
)


def check_memory():
    try:
        result = subprocess.run(
            ["free", "-m"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        for line in result.stdout.splitlines():
            if line.startswith("Mem:"):
                words = line.split()
                available = words[-1]
                break

        if int(available) > 500:
            logging.info(f"Available Memory : {available}")
        else:
            logging.warning(
                f"Available Memory : {available} - Low Memory"
            )

    except subprocess.SubprocessError as e:
        logging.error(e)


def check_disk():
    try:
        result = subprocess.run(
            ["df", "-h"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        for line in result.stdout.splitlines():
            if line.endswith(" /"):
                words = line.split()
                usage = words[-2].removesuffix("%")
                break

        if int(usage) > 90:
            logging.warning(f"Disk Usage : {usage}%")
        else:
            logging.info(f"Disk Usage : {usage}%")

    except subprocess.SubprocessError as e:
        logging.error(e)

def check_cpu():
    try:
        result = subprocess.run(
            ["uptime"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        logging.info(f"CPU Load : {result.stdout.strip()}")

    except subprocess.SubprocessError as e:
        logging.error(e)



def check_hostname():
    try:
        result = subprocess.run(
            ["hostname"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        logging.info(f"Hostname : {result.stdout.strip()}")

    except subprocess.SubprocessError as e:
        logging.error(e)


def check_current_user():
    try:
        result = subprocess.run(
            ["whoami"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        logging.info(f"Current User : {result.stdout.strip()}")

    except subprocess.SubprocessError as e:
        logging.error(e)


def check_service(service_name):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.stdout.strip() == "active":
            logging.info(f"Service {service_name} : RUNNING")
        else:
            logging.error(f"Service {service_name} : NOT RUNNING")

    except subprocess.SubprocessError as e:
        logging.error(e)