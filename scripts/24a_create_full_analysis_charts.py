
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")

data_path = Path("data/processed")

data = pd.read_csv(data_path / "full_result_distribution.csv")

print(data.head(1))

data.sort_values(
    by="total_by_result",
    ascending=False,
    inplace=True
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=data,
            x="result",
            y="total_by_result",
            color="#6A9FB5",
            ax=ax)

for container in ax.containers:
    ax.bar_label(container,
                 fmt="{:,.0f}",
                 padding=4,
                 color="#0b4a52",
                 fontsize=10
                 )

plt.title("Chicago Food Inspection Results")
plt.xlabel("Inspection result")
plt.ylabel("Total inspections")
ax.set_ylim(0, data["total_by_result"].max() * 1.15)
ax.tick_params(axis="x", rotation=35)

plt.tight_layout()

# Save plot in images folder
output_path = Path("images/full_result_distribution.png")
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path,
            dpi=300,
            bbox_inches="tight")


plt.show()

print("Output path:", output_path)