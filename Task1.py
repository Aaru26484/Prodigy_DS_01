import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Adjust path if needed
csv_path = 'raw_merged_heart_dataset.csv'

df = pd.read_csv(csv_path)

# --- Age histogram (continuous) ---
plt.figure(figsize=(8, 5))
sns.histplot(df['age'].dropna(), bins=20, kde=True, color='tab:blue')
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('age_histogram.png', dpi=150)
plt.show()

# --- Sex bar chart (categorical) ---
sex_col = 'sex'  # change if column name differs

# Try mapping common encodings 0/1 -> Female/Male
if sex_col in df.columns:
    try:
        mapped = df[sex_col].map({0: 'Female', 1: 'Male'})
        if mapped.isna().all():
            counts = df[sex_col].astype(str).value_counts()
            labels = counts.index.tolist()
            values = counts.values
        else:
            counts = mapped.fillna(df[sex_col].astype(str)).value_counts()
            labels = counts.index.tolist()
            values = counts.values
    except Exception:
        counts = df[sex_col].astype(str).value_counts()
        labels = counts.index.tolist()
        values = counts.values

    plt.figure(figsize=(6, 4))
    sns.barplot(x=labels, y=values, palette='pastel')
    plt.title('Sex distribution')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('sex_barchart.png', dpi=150)
    plt.show()
else:
    print(f"Column `{sex_col}` not found in {csv_path}. Available columns: {list(df.columns)}")