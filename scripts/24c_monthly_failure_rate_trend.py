# Create a time-series chart of monthly failure rates and the 12-month trend.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")

input_path = Path("data/processed/full_monthly_inspection_summary.csv")
output_path = Path("images/full_monthly_failure_trend.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(input_path)
data["inspection_month"] = pd.to_datetime(data["inspection_month"])
data["failure_rolling_avg"] = (
    data["failure_rate_pct"].rolling(window=12, min_periods=12).mean()
)

fig, ax = plt.subplots(figsize=(11, 6))

sns.lineplot(
    data=data,
    x="inspection_month",
    y="failure_rate_pct",
    color="#9ECAE1",
    label="Failure rate (%)",
    linewidth=1.5,
    ax=ax,
)

sns.lineplot(
    data=data,
    x="inspection_month",
    y="failure_rolling_avg",
    color="#265F7C",
    label="12-month rolling average",
    linewidth=3,
    ax=ax,
)

ax.set_title("Monthly Food Inspection Failure Rate", fontsize=16, pad=14)
ax.set_xlabel("Inspection month", fontsize=12)
ax.set_ylabel("Failure rate (%)", fontsize=12)

plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("Output path:", output_path)
