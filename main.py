import json
from datetime import datetime

def transform_format_1(entry):
    return {
        "device_id": entry["device"],
        "timestamp": entry["time"],  # already in ms
        "temperature": entry["temp"],
        "pressure": entry["press"],
        "status": entry["status"]
    }

def transform_format_2(entry):
    # timestamp ISO → ms
    ts = int(datetime.fromisoformat(entry["timestamp"].replace("Z","")).timestamp() * 1000)
    return {
        "device_id": entry["id"],
        "timestamp": ts,
        "temperature": entry["temperature_value"],
        "pressure": entry["psi"],
        "status": entry["status"]
    }

def load_and_transform(filename, transformer):
    with open(filename, "r") as f:
        data = json.load(f)
    return [transformer(d) for d in data]

def main():
    result = []
    result += load_and_transform("data-1.json", transform_format_1)
    result += load_and_transform("data-2.json", transform_format_2)

    with open("output.json", "w") as f:
        json.dump(result, f, indent=2)

    print("✅ Output written to output.json")

if __name__ == "__main__":
    main()




