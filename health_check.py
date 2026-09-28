#!/usr/bin/env python3

import subprocess
import logging
import shutil


# ---------------------------------
# Logging Configuration
# ---------------------------------
logging.basicConfig(
    filename="healthcheck.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------------
# Run Linux Command
# ---------------------------------
def run_command(command):
    try:
        return subprocess.getoutput(command)
    except Exception as error:
        return f"Error: {error}"


# ---------------------------------
# Server Uptime Check
# ---------------------------------
def check_uptime():
    print("\n[1] Server Uptime")

    uptime = run_command("uptime -p")

    print(uptime)
    logging.info(f"Server Uptime: {uptime}")


# ---------------------------------
# CPU Usage Check
# ---------------------------------
def check_cpu():
    print("\n[2] CPU Usage")

    cpu = run_command(
        "top -bn1 | grep '%Cpu' | awk '{print $2}'"
    )

    print(f"CPU Usage: {cpu}%")
    logging.info(f"CPU Usage: {cpu}%")


# ---------------------------------
# Memory Usage Check
# ---------------------------------
def check_memory():
    print("\n[3] Memory Usage")

    memory = run_command("free -h")

    print(memory)
    logging.info("Memory Usage:")
    logging.info(memory)


# ---------------------------------
# Disk Usage Check
# ---------------------------------
def check_disk():
    print("\n[4] Disk Usage")

    disk = run_command("df -h")

    print(disk)

    logging.info("Disk Usage:")
    logging.info(disk)


# ---------------------------------
# Top Processes Check
# ---------------------------------
def check_processes():
    print("\n[5] Top 5 Memory Consuming Processes")

    processes = run_command(
        "ps aux --sort=-%mem | head -6"
    )

    print(processes)

    logging.info("Top Processes:")
    logging.info(processes)


# ---------------------------------
# Disk Alert Check
# ---------------------------------
def check_disk_alert():

    total, used, free = shutil.disk_usage("/")

    usage_percentage = (used / total) * 100

    print("\n[6] Disk Alert Status")

    if usage_percentage > 80:
        message = (
            f"WARNING: Disk Usage Above 80% "
            f"({usage_percentage:.2f}%)"
        )
        print(message)
        logging.warning(message)

    else:
        message = (
            f"Disk Usage Normal "
            f"({usage_percentage:.2f}%)"
        )
        print(message)
        logging.info(message)


# ---------------------------------
# Main Function
# ---------------------------------
def main():

    print("=" * 60)
    print("        Linux Server Health Check Script")
    print("=" * 60)

    logging.info(
        "========== Health Check Started =========="
    )

    check_uptime()
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    check_disk_alert()

    print("\nHealth Check Completed Successfully")

    logging.info(
        "========== Health Check Completed =========="
    )


# ---------------------------------
# Program Entry Point
# ---------------------------------
if __name__ == "__main__":
    main()