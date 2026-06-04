# Create a horizontal bar chart of ZIP codes with the highest failure rates.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")

input_path = Path("data/processed/full_zip_failure_rates.csv")
output_path = Path("images/full_zip_failure_rates.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(input_path)
data["zip"] = data["zip"].astype(str)
data = data.sort_values(by="failure_rate_pct", ascending=False)
top_zip_codes = data.head(10)

fig, ax = plt.subplots(figsize=(11, 6))

sns.barplot(
    data=top_zip_codes,
    y="zip",
    x="failure_rate_pct",
    color="#C77C9C",
    edgecolor="white",
    linewidth=1,
    ax=ax,
)

ax.bar_label(
    ax.containers[0],
    labels=[f"{value:.1f}%" for value in top_zip_codes["failure_rate_pct"]],
    padding=4,
    fontsize=10,
    color="#263238",
)

ax.set_title("ZIP Codes With Highest Food Inspection Failure Rates", fontsize=16, pad=14)
ax.set_xlabel("Failure rate (%)", fontsize=12)
ax.set_ylabel("ZIP code", fontsize=12)
ax.set_xlim(0, top_zip_codes["failure_rate_pct"].max() * 1.12)

plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("Output path:", output_path)
