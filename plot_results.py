import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

with open("results.csv", newline="") as f:
    rows = list(csv.DictReader(f))

def make_plot(column, ylabel, title, filename):
    valid_rows = [
        r for r in rows
        if r.get(column, "").strip()
        and r.get("scenario", "").strip()
    ]

    scenarios = [r["scenario"] for r in valid_rows]
    values = [float(r[column]) for r in valid_rows]

    plt.figure(figsize=(8, 5))
    plt.bar(scenarios, values)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved {filename}")

make_plot("average_rtt_ms", "Average RTT (ms)",
          "Network RTT Comparison", "rtt_comparison.png")
make_plot("packet_loss_percent", "Packet loss (%)",
          "Packet Loss Comparison", "packet_loss_comparison.png")
make_plot("http_total_time_ms", "HTTP total time (ms)",
          "HTTP Response Time Comparison", "http_time_comparison.png")
