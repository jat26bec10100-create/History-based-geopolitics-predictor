# Advanced 3-Parameter Risk Scoring Engine

## About the Project
The **Advanced 3-Parameter Risk Scoring Engine** is a terminal-based computational model written in Python. It transitions from basic proximity matching toward a structured mathematical risk framework using linear combinations. 

The system accepts real-time numeric inputs for critical indicator metrics, applies custom algorithmic weights, and maps the resulting continuous score to a clear operational risk category.

## Features
* **From-Scratch Mathematical Modeling:** Uses pure mathematical linear combination formulas without depending on external libraries or large-scale datasets.
* **System Importance Weights:** Explicitly balances economic, strategic, and resource-based components using explicit floating-point weights.
* **Algorithmic Classification:** Maps the finalized scalar threat metric onto categorical system-stability tiers.

---

## Technical Architecture & Core Logic

### 1. Risk Parameters and Component Balancing
The mathematical engine weighs three core indicators based on their structural importance:

| Indicator Metric | Operational Mapping | Assigned Weight |
| :--- | :--- | :--- |
| **Inflation Level** | Economic Instability | `0.20` |
| **Border Tension Level** | Geopolitical Conflict | `0.30` |
| **Resource Scarcity Level** | Supply Chain Vulnerability | `0.50` |

*Note: Resource Scarcity maintains the highest priority weight (`0.50`) within this computational model.*

### 2. The Mathematical Equation
The program processes the inputs directly through a custom formula. Each indicator is scaled from `1.0` (Low Risk) to `10.0` (Extreme Risk). The raw score is multiplied by `10` at the end to convert the 1–10 scale into a **percentage-based Threat Index scale of 10.0 to 100.0**:

\[\text{Raw Weighted Score} = (\text{Inflation} \times 0.20) + (\text{Tension} \times 0.30) + (\text{Scarcity} \times 0.50)\]

\[\text{Final Threat Index} = \text{Raw Weighted Score} \times 10\]

### 3. Classification Thresholds
The continuous mathematical score is passed through a boundary evaluation system to finalize the structural risk categorization:

* **≥ 75.0** → `CRITICAL RISK: Structural Breakdown / High Conflict Probability`
* **≥ 45.0 and < 75.0** → `MODERATE RISK: Elevated instability, diplomatic intervention required`
* **< 45.0** → `STABLE: System operating within manageable parameters`

---

## Operational Verification (Execution Example)

If the system indicators are evaluated with the following values:
* **Current Inflation Level:** `6.0`
* **Current Border Tension Level:** `8.0`
* **Current Resource Scarcity Level:** `7.0`

### Computational Step-by-Step:
1. **Raw Aggregation:** (6.0 × 0.20) + (8.0 × 0.30) + (7.0 × 0.50) = 1.2 + 2.4 + 3.5 = 7.1
2. **Scale Normalization:** 7.1 × 10 = 71.00
3. **Classification Check:** 71.00 falls between the 45.0 and 75.0 thresholds.

### Expected Terminal Output:
```text
=== ADVANCED 3-PARAMETER RISK SCORING ENGINE ===

Rate the current indicators on a scale of 1.0 (Low Risk) to 10.0 (Extreme Risk):
1. Current Inflation Level (1-10): 6.0
2. Current Border Tension Level (1-10): 8.0
3. Current Resource Scarcity Level (1-10): 7.0

==================================================
             COMPUTATIONAL RISK REPORT             
==================================================
Calculated Threat Index : 71.00 / 100.00
Algorithmic Conclusion  : MODERATE RISK: Elevated instability, diplomatic intervention required
==================================================
```

---

## How to Run the Engine

### Prerequisites
* **Python 3.x** environment installed.

### Execution Steps
1. Clone or download the repository script files.
2. Open your operating system's terminal or command prompt inside the project folder.
3. Launch the script using the interpreter:
   ```bash
   python risk_engine.py
   ```
4. Input your floating-point metric ratings when prompted by the terminal engine.

## Technologies Applied
* **Language:** Python 3 (Standard Library Only)
* **Programming Paradigm:** Procedural Programming
* **Core Concepts:** Type Casting (`float`), Linear Combination Mechanics, Arithmetic Assignment Operators, Logical Conditional Branching (`if-elif-else`).

## Academic Disclaimer
This software functions purely as a deterministic computational exercise demonstrating linear combination mechanics and basic conditional logic. The generated threat outputs are defined strictly by user inputs and hardcoded weights; they do not constitute empirical forecasts, real-world statistical predictions, or professional risk evaluations.
