# =====================================================================
# RESEARCH ENGINE: MULTI-PARAMETER WEIGHTED INDEXING (FROM SCRATCH)
# Moving from simple proximity matching to mathematical risk equations
# =====================================================================

print("=== ADVANCED 3-PARAMETER RISK SCORING ENGINE ===")

# 1. DEFINE SYSTEM WEIGHTS (Importance metrics)
# These represent the structural rules of our mathematical model
WEIGHT_INFLATION = 0.20

WEIGHT_TENSION   = 0.30
WEIGHT_SCARCITY  = 0.50

# 2. COLLECT 3 PARAMETERS FROM THE USER
print("\nRate the current indicators on a scale of 1.0 (Low Risk) to 10.0 (Extreme Risk):")
val_inflation = float(input("1. Current Inflation Level (1-10): "))
val_tension   = float(input("2. Current Border Tension Level (1-10): "))
val_scarcity  = float(input("3. Current Resource Scarcity Level (1-10): "))

# 3. THE MATHEMATICAL ENGINE (Linear Combination / Weighted Scoring)
# Instead of comparing to old dots, we pass the inputs directly through a custom formula.
# We multiply each value by 10 at the end to turn a scale of 1-10 into a percentage scale of 10-100.

raw_weighted_score = (val_inflation * WEIGHT_INFLATION) + (val_tension * WEIGHT_TENSION) + (val_scarcity * WEIGHT_SCARCITY)
final_threat_index = raw_weighted_score * 10 

# 4. ALGORITHMIC CLASSIFICATION SYSTEM
# The computer maps the continuous mathematical score to a risk category
if final_threat_index >= 75.0:
    risk_category = "CRITICAL RISK: Structural Breakdown / High Conflict Probability"
elif final_threat_index >= 45.0:
    risk_category = "MODERATE RISK: Elevated instability, diplomatic intervention required"
else:
    risk_category = "STABLE: System operating within manageable parameters"

# 5. PRINT THE RESEARCH REPORT
print("\n" + "="*50)
print("             COMPUTATIONAL RISK REPORT             ")
print("="*50)
print(f"Calculated Threat Index : {final_threat_index:.2f} / 100.00")
print(f"Algorithmic Conclusion  : {risk_category}")
print("="*50)
