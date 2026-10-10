import csv
import matplotlib.pyplot as plt

with open("results.csv", newline="") as f:
    rows = list(csv.DictReader(f))

scenarios = [r["scenario"] for r in rows]
rtt = [float(r["average_rtt_ms"]) for r in rows]
loss = [float(r["packet_loss_percent"]) for r in rows]
http = [float(r["http_total_time_ms"]) for r in rows]

def make_plot(values, ylabel, title, filename):
    plt.figure(figsize=(8, 5))
    plt.bar(scenarios, values)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved {filename}")

make_plot(rtt, "Average RTT (ms)", "Network RTT Comparison", "rtt_comparison.png")
make_plot(loss, "Packet loss (%)", "Packet Loss Comparison", "packet_loss_comparison.png")
make_plot(http, "HTTP total time (ms)", "HTTP Response Time Comparison", "http_time_comparison.png")
