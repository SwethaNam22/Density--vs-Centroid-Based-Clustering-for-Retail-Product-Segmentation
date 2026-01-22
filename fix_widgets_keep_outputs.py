import json
from pathlib import Path

notebooks = [
    "amazon10k_clustering_analysis_dev.ipynb",
    "amazon60k_clustering_analysis_dev.ipynb",
]

for nb_name in notebooks:
    path = Path(nb_name)

    if not path.exists():
        print(f"❌ File not found: {nb_name}")
        continue

    nb = json.loads(path.read_text(encoding="utf-8"))

    # Remove notebook-level widget metadata
    nb.get("metadata", {}).pop("widgets", None)

    # Remove any cell-level widget metadata
    for cell in nb.get("cells", []):
        cell.get("metadata", {}).pop("widgets", None)

    path.write_text(
        json.dumps(nb, ensure_ascii=False, indent=1),
        encoding="utf-8"
    )

    print(f" Fixed widgets metadata (kept outputs): {nb_name}")
