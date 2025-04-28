#!/usr/bin/env python3

import subprocess
import os


def get_cpu_usage():
    try:
        output = subprocess.check_output(["ps", "-A", "-o", "%cpu"], text=True)
        cpu_usages = output.strip().split("\n")[1:]
        cpu_usages = [float(usage) for usage in cpu_usages if usage]
        total_cpu = sum(cpu_usages)
        core_count = os.cpu_count() or 1  # fallback to 1 if unavailable
        normalized_cpu = total_cpu / core_count
        return round(normalized_cpu, 1)
    except Exception:
        return "Err"


def main():
    cpu = get_cpu_usage()
    if isinstance(cpu, (int, float)):
        cpu_int = int(cpu)
        print(f"{cpu_int}% CPU")
    else:
        print(f"CPU: {cpu}")
    print("---")
    try:
        output = subprocess.check_output(
            ["/bin/ps", "-Ao", "pid,args,pcpu,rss"], text=True
        )
        lines = output.strip().split("\n")[1:]
        processes = []
        core_count = os.cpu_count() or 1
        for line in lines:
            fields = line.strip().split()
            if len(fields) >= 4:
                pid = fields[0]
                command_full = " ".join(fields[1:-2])
                cpu_usage_raw = float(fields[-2])
                cpu_usage = cpu_usage_raw / core_count
                rss = int(fields[-1])
                processes.append((pid, command_full, cpu_usage, rss))

        processes.sort(key=lambda p: -p[2])

        print(f"CPU Load: {cpu_int}% | color=black")
        print("Refresh Now | refresh=true")
        print("---")

        for pid, command_full, cpu_usage, rss in processes[:10]:
            # Extract just the instance name
            instance = command_full.split('/')[-1] or command_full
            mem_mb = round(rss / 1024)
            ram_warning = " 🐘" if mem_mb > 1000 else ""

            # Color code CPU load
            if cpu_usage > 50:
                color = "red"
            elif cpu_usage > 20:
                color = "orange"
            elif cpu_usage > 10:
                color = "yellow"
            else:
                color = "gray"

            # Display instance with correct color directive (only one | color=...)
            print(f"{instance} ({cpu_usage:.1f}%, {mem_mb}MB{ram_warning}) | color={color}")

            # Cascade menu under instance
            path_to_open = os.path.dirname(command_full)
            if not path_to_open or path_to_open == '/':
                path_to_open = command_full
            print(f"--📂 Open in Finder | bash='open \"{path_to_open}\"' terminal=false refresh=false")
            print(f"--❗ Kill Instance | bash='/bin/bash' param1=-c param2='if /usr/bin/osascript -e \"tell application \\\"System Events\\\" to display dialog \\\"Kill this process?\\\\n{instance}\\\\nCPU: {cpu_usage:.1f}% | Memory: {mem_mb}MB\\\\nPID: {pid}\\\" buttons {{\\\"Cancel\\\",\\\"Kill\\\"}} default button \\\"Cancel\\\"\" | grep -q \"button returned:Kill\"; then kill {pid}; fi' terminal=false refresh=true")
            print(f"--ℹ️ Show Details | bash=/bin/ps param1=-p param2={pid} param3=-o param4=pid,ppid,%cpu,%mem,nice,lstart,etime,command terminal=true refresh=false")

        print("---")
    except Exception:
        print("Unable to list processes | color=red")


if __name__ == "__main__":
    main()
