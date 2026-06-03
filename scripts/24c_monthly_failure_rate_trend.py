from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")

data_path = Path("data/processed")

data = pd.read_csv(data_path / "full_monthly_inspection_summary.csv")

# Convert inspection_month to datetime
data["inspection_month"] = pd.to_datetime(data["inspection_month"])

# Compute the 12-month rolling average
data["failure_rolling_avg"] = (
    data["failure_rate_pct"].rolling(window=12, min_periods=12).mean()
)

print(data)

fig, ax = plt.subplots(figsize=(10, 6))

sns.lineplot(data = data,
             x="inspection_month",
             y="failure_rate_pct",
             marker=None,
             color="#9ecae1",
             label="Failure rate (%)",
             linewidth=1.5,
             ax=ax
             )

sns.lineplot(data = data,
             x="inspection_month",
             y="failure_rolling_avg",
             marker=None,
             color="#265f7c",
             label="12-month rolling average",
             linewidth=3,
             ax=ax
             )

plt.title("Monthly Food Inspection Failure Rate")
plt.ylabel("Failure rate (%)")
plt.xlabel("Inspection month")

plt.tight_layout()

# Save plot in images folder
output_path = Path("images/full_monthly_failure_trend.png")
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path,
            dpi=300,
            bbox_inches="tight")

plt.show()

print("Output path:", output_path)