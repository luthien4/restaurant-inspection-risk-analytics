from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")

data_path = Path("data/processed")

data = pd.read_csv(data_path / "full_zip_failure_rates.csv")

data["zip"] = data["zip"].astype(str)

data.sort_values(
    by="failure_rate_pct",
    ascending=False,
    inplace=True
)

data_top10 = data.head(10)

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(data=data_top10,
            y="zip",
            x="failure_rate_pct",
            color="#e27b9b",
            edgecolor="white",
            linewidth=1,
            ax=ax
            )

# for container in ax.containers:
ax.bar_label(ax.containers[0],
             labels=[f"{value:.1f}%" for value in data_top10["failure_rate_pct"]],
             padding=4,
             fontsize=10,
             )

plt.title("ZIP Codes With Highest Food Inspection Failure Rates")
plt.xlabel("Failure rate (%)")
plt.ylabel("ZIP code")
ax.set_xlim(0, data_top10["failure_rate_pct"].max() * 1.12)

plt.tight_layout()

# Save plot in images folder
output_path = Path("images/full_zip_failure_rates.png")
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path,
            dpi=300,
            bbox_inches="tight")

plt.show()

print("Output path:", output_path)