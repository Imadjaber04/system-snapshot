import platform
import shutil
from datetime import datetime


def bytes_to_gb(n):
    return round(n / (1024**3), 2)


def get_system_snapshot():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os_name = platform.system()
    os_version = platform.release()
    machine = platform.machine()

    total, used, free = shutil.disk_usage("/")
    used_percent = round((used / total) * 100, 2)

    report = []
    report.append("=== System Health Snapshot ===")
    report.append(f"Time: {now}")
    report.append(f"OS: {os_name} {os_version}")
    report.append(f"Machine: {machine}")
    report.append("")
    report.append("=== Disk Usage (/) ===")
    report.append(f"Total: {bytes_to_gb(total)} GB")
    report.append(f"Used : {bytes_to_gb(used)} GB")
    report.append(f"Free : {bytes_to_gb(free)} GB")
    report.append(f"Used %: {used_percent}%")

    return "\n".join(report)


def save_report(text):
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(text)
    return filename


def main():
    snapshot = get_system_snapshot()
    print(snapshot)

    saved_as = save_report(snapshot)
    print(f"\nSaved report to: {saved_as}")


if __name__ == "__main__":
    main()
