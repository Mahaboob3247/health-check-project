import subprocess

print("=" * 50)
print(" Linux Server Health Check ")
print("=" * 50)

# Check Uptime
print("\n[1] Server Uptime")
uptime = subprocess.getoutput("uptime -p")
print(uptime)

# Check CPU Usage
print("\n[2] CPU Usage")
cpu = subprocess.getoutput(
    "top -bn1 | grep '%Cpu' | awk '{print $2}'"
)
print(f"CPU Usage: {cpu}%")

# Check Memory Usage
print("\n[3] Memory Usage")
memory = subprocess.getoutput("free -h")
print(memory)

# Check Disk Usage
print("\n[4] Disk Usage")
disk = subprocess.getoutput("df -h")
print(disk)

# Top 5 Memory Consuming Processes
print("\n[5] Top 5 Memory Processes")
processes = subprocess.getoutput(
    "ps aux --sort=-%mem | head -6"
)
print(processes)

print("\nHealth Check Completed Successfully")

import logging
import subprocess

logging.basicConfig(
    filename="healthcheck.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

disk = subprocess.getoutput("df -h")

logging.info("Disk Check Executed")
logging.info(disk)

print("Check healthcheck.log")



import shutil

total, used, free = shutil.disk_usage("/")

usage = used / total * 100

if usage > 80:
    print("WARNING : Disk Usage Above 80%")
else:
    print("Disk Usage Normal")