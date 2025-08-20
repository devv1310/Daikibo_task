# Daikibo Industrials - IIoT Data Normalization

This project is a coding challenge for **Daikibo Industrials**, where multiple IIoT devices send telemetry data in different formats.  
The goal is to **unify data from different formats into a single standard format** for monitoring and analysis.

---

## 🚀 Project Overview

- **Problem**:  
  Half of the IIoT devices send telemetry data in one format (`data-1.json`), and the other half in another format (`data-2.json`).  
  These formats need to be **converted into a unified format** as shown in `data-result.json`.

- **Solution**:  
  A Python script (`main.py`) that:
  1. Reads `data-1.json` and `data-2.json`  
  2. Transforms them into the target schema  
  3. Handles **timestamp conversion** (ISO ↔ milliseconds)  
  4. Outputs a unified file (`output.json`)  

---

## 📂 Project Structure


---

## ⚙️ How It Works

### Mapping Example

| data-1.json        | data-2.json          | unified format (data-result.json) |
|--------------------|----------------------|-----------------------------------|
| `device`           | `id`                 | `device_id`                       |
| `time` (ms)        | `timestamp` (ISO)    | `timestamp` (ms)                  |
| `temp`             | `temperature_value`  | `temperature`                     |
| `press`            | `psi`                | `pressure`                        |
| `status`           | `status`             | `status`                          |

---

## ▶️ How to Run

1. **Fork the project** on [Replit](https://replit.com) or clone it locally.  
2. Open `main.py` and review the field mappings.  
3. Run the script:

```bash
python main.py
