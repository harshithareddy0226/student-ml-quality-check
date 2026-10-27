
import json
import sys

MINIMUM_ACCURACY = 0.85

print("Reading model evaluation metrics...")

try:
    with open("metrics.json", "r") as file:
        metrics = json.load(file)

    accuracy = float(metrics["accuracy"])

    if not 0.0 <= accuracy <= 1.0:
        raise ValueError("Accuracy must be between 0 and 1.")

except (
    OSError,
    json.JSONDecodeError,
    KeyError,
    TypeError,
    ValueError
) as error:
    print("QUALITY GATE FAILED")
    print("Unable to read valid model accuracy:", error)
    sys.exit(1)

print("Model Accuracy:", round(accuracy, 4))
print("Required Accuracy:", MINIMUM_ACCURACY)

if accuracy < MINIMUM_ACCURACY:
    print("QUALITY GATE FAILED")
    print("Model performance is below the required threshold.")
    sys.exit(1)

print("QUALITY GATE PASSED")
print("Model performance satisfies the required threshold.")
sys.exit(0)
