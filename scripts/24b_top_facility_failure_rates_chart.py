# Create a horizontal bar chart of facility types with the highest failure rates.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")

input_path = Path("data/processed/full_facility_failure_rates.csv")
output_path = Path("images/full_facility_failure_rates.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(input_path)
data = data.sort_values(by="failure_rate_pct", ascending=False)
top_facilities = data.head(10)

fig, ax = plt.subplots(figsize=(11, 6))

sns.barplot(
    data=top_facilities,
    y="facility_type",
    x="failure_rate_pct",
    color="#8DBB8C",
    edgecolor="white",
    linewidth=1,
    ax=ax,
)

ax.bar_label(
    ax.containers[0],
    labels=[f"{value:.1f}%" for value in top_facilities["failure_rate_pct"]],
    padding=4,
    fontsize=10,
    color="#263238",
)

ax.set_title("Facility Types With Highest Failure Rates", fontsize=16, pad=14)
ax.set_xlabel("Failure rate (%)", fontsize=12)
ax.set_ylabel("Facility type", fontsize=12)
ax.set_xlim(0, top_facilities["failure_rate_pct"].max() * 1.12)

plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("Output path:", output_path)
