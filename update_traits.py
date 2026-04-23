#!/usr/bin/env python3
"""
update_traits.py - Extract FELINE and generic mutations from CDDA.
Only mutations with category containing 'FELINE' or no category are included.
"""

import json
import os
from pathlib import Path

CDDA_ROOT = Path(os.environ.get("CDDA_ROOT", "cdda"))
MOD_SCENARIO_FILE = Path("scenarios.json")

EXCLUDE_IDS = {
    "MUTAGEN_GLAND_ABSTRACT",
    "EATHEALTH_active",
    "BIOLUM1_active",
    "BIOLUM2_active",
    "CLAWS_RETRACT_active",
    "WINGS_INSECT_active",
    "CHANGING",
    # Add any threshold markers if they accidentally appear
    "THRESH_FELINE",
    "THRESH_ALPHA",
    "THRESH_BATRACHIAN",
    # ... (optional: add all other THRESH_* to be safe)
}

def is_feline_or_generic(item):
    """Return True if mutation should be included."""
    mid = item["id"]
    if mid in EXCLUDE_IDS:
        return False

    category = item.get("category")
    # If category is missing, it's a generic mutation (like TOUGH)
    if not category:
        return True
    # If category contains 'FELINE', include it
    if "FELINE" in category:
        return True
    # Exclude everything else (other lines, thresholds)
    return False

def collect_mutation_ids():
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
                    if is_feline_or_generic(item):
                        ids.add(item["id"])
    return sorted(ids)

def main():
    ids = collect_mutation_ids()
    print(f"Collected {len(ids)} FELINE/generic mutation IDs.")
    with open(MOD_SCENARIO_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data[0]["extend"]["traits"] = ids
    with open(MOD_SCENARIO_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {MOD_SCENARIO_FILE}.")

if __name__ == "__main__":
    main()
