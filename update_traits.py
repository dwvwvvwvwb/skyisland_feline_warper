#!/usr/bin/env python3
"""
update_traits.py - Extract all mutation IDs from CDDA and update scenario.
No filtering except internal pseudo-mutations.
"""

import json
import os
from pathlib import Path

CDDA_ROOT = Path(os.environ.get("CDDA_ROOT", "cdda"))
MOD_SCENARIO_FILE = Path("scenarios.json")

# Exclude only internal pseudo-mutations
EXCLUDE_IDS = {
    "MUTAGEN_GLAND_ABSTRACT",
    "EATHEALTH_active",
    "BIOLUM1_active",
    "BIOLUM2_active",
    "CLAWS_RETRACT_active",
    "WINGS_INSECT_active",
    "CHANGING",
}

def collect_mutation_ids():
    """Traverse CDDA JSON files and collect all type:mutation ids."""
    ids = set()
    patterns = ["data/json/mutations/*.json", "data/mods/extra_mut_scen/*.json"]
    for pattern in patterns:
        for f in CDDA_ROOT.glob(pattern):
            try:
                data = json.load(open(f, encoding='utf-8'))
            except:
                continue
            items = data if isinstance(data, list) else [data]
            for item in items:
                if item.get("type") == "mutation" and "id" in item:
                    mid = item["id"]
                    if mid not in EXCLUDE_IDS:
                        ids.add(mid)
    return sorted(ids)

def main():
    ids = collect_mutation_ids()
    print(f"Collected {len(ids)} mutation IDs.")
    with open(MOD_SCENARIO_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data[0]["extend"]["traits"] = ids
    with open(MOD_SCENARIO_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {MOD_SCENARIO_FILE} with {len(ids)} traits.")

if __name__ == "__main__":
    main()