from datetime import datetime

def analyze_heartbeat_log(input_file='hblog.txt', output_file='hb_test.log', key='TSTFEED0300|7E3E|0400'):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered = [line for line in lines if key in line]

    timestamps = []
    for line in filtered:
        idx = line.find("Timestamp ")
        if idx != -1:
            try:
                ts_str = line[idx + 10:idx + 18]
                ts = datetime.strptime(ts_str, "%H:%M:%S")
                timestamps.append((ts, line.strip()))
            except ValueError:
                continue

    with open(output_file, 'w') as out:
        for i in range(len(timestamps) - 1):
            t1, line1 = timestamps[i]
            t2, _ = timestamps[i + 1]
            diff = abs((t2 - t1).total_seconds())
            if 31 < diff < 33:
                out.write(f"[WARNING] Heartbeat delay {diff:.1f}s at {t1.time()} — {line1}\n")
            elif diff >= 33:
                out.write(f"[ERROR] Heartbeat delay {diff:.1f}s at {t1.time()} — {line1}\n")


if __name__ == "__main__":
    analyze_heartbeat_log("hblog.txt", "hb_test.log")
    print("Analysis complete. Check hb_test.log.")