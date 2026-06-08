"""
Reads doubles_slots.csv and injects teamSlots: { 1: [...], 2: [...] }
into trainer_metadata.js by parsing it as structured data.
"""

import csv
import json
import subprocess

CSV_PATH       = "./scripts/data/doublesSlots.csv"
METADATA_PATH  = "./src/js/data/trainer_metadata.js"
JSON_PATH      = "./scripts/data/trainerMetadata.json"
EXPORT_SCRIPT = "./scripts/exportTrainerMetadata.sh"


def parse_poks(cell):
    return [p.strip() for p in cell.split(",") if p.strip()]


def load_slots(path):
    slots = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            slots[row["Trainer"]] = {
                "1": parse_poks(row["Slot 1"]),
                "2": parse_poks(row["Slot 2"]),
            }
    return slots


def load_metadata(json_path):
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


def js_slots_obj(team_slots):
    """Render { "PokeName": slotNum, ... } as a JS object literal."""
    parts = ', '.join(f'"{k}": {v}' for k, v in team_slots.items())
    return '{ ' + parts + ' }'


def write_metadata(path, data):
    true_trainers   = [(k, v) for k, v in data.items() if v.get('battleType') == 'true']
    pseudo_trainers = [(k, v) for k, v in data.items() if v.get('battleType') == 'pseudo']

    def entry(trainer, props):
        ts = props.get('teamSlots', {})
        battle = props['battleType']
        return (
            f'\t"{trainer}": '
            f'{{ isDouble: true, battleType: "{battle}", '
            f'teamSlots: {js_slots_obj(ts)} }},'
        )

    lines = [
        'var TRAINER_METADATA = {',
        '\t// true double battles (single team, both trainers act as one)',
    ]
    lines += [entry(k, v) for k, v in true_trainers]
    lines += [
        '',
        '\t// pseudo double battles (two separate trainers, each contributes their own slot)',
    ]
    lines += [entry(k, v) for k, v in pseudo_trainers]
    lines += ['};', '']

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    subprocess.run(["bash", EXPORT_SCRIPT], check=True)

    slots = load_slots(CSV_PATH)
    print(f"Loaded {len(slots)} trainers from CSV")

    data = load_metadata(JSON_PATH)
    print(f"Parsed {len(data)} trainers from metadata")

    updated = 0
    for trainer, s in slots.items():
        if trainer in data:
            team_slots = {}
            for pok in s['1']:
                team_slots[pok] = 1
            for pok in s['2']:
                team_slots[pok] = 2
            data[trainer]['teamSlots'] = team_slots
            updated += 1
        else:
            print(f"WARNING: '{trainer}' not found in metadata")

    write_metadata(METADATA_PATH, data)
    print(f"Updated {updated} entries in trainer_metadata.js")


if __name__ == "__main__":
    main()
