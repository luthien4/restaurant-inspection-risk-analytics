# Create a bar chart showing inspection result distribution.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")

input_path = Path("data/processed/full_result_distribution.csv")
output_path = Path("images/full_result_distribution.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(input_path)
data = data.sort_values(by="total_by_result", ascending=False)

fig, ax = plt.subplots(figsize=(11, 6))

sns.barplot(
    data=data,
    x="result",
    y="total_by_result",
    color="#6A9FB5",
    ax=ax,
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="{:,.0f}",
        padding=4,
        color="#263238",
        fontsize=10,
    )

ax.set_title("Chicago Food Inspection Results", fontsize=16, pad=14)
ax.set_xlabel("Inspection result", fontsize=12)
ax.set_ylabel("Total inspections", fontsize=12)
ax.set_ylim(0, data["total_by_result"].max() * 1.15)
ax.tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("Output path:", output_path)
