import argparse
import pandas as pd
import numpy as np
import sys


def check_mean_drift(data, expected_mean, threshold=1.0):
    """Check if the mean of data drifts beyond a threshold from expected_mean.
    Args:
        data (list[float]): The data to check.
        expected_mean (float): The expected mean value.
        threshold (float): Allowed drift before failure.
    Returns:
        bool: True if drift is within threshold, False otherwise.
    """
    actual_mean = np.mean(data)
    drift = abs(actual_mean - expected_mean)
    print(f"Actual mean: {actual_mean}, "
          f"Expected mean: {expected_mean}, Drift: {drift}")
    return drift <= threshold


if __name__ == "__main__":
    # Example: python drift_check.py --csv sample_data.csv
    # --column age_int --expected_mean 30 --threshold 0.0
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, required=True,
                        help='CSV file path')
    parser.add_argument('--column', type=str, required=True,
                        help='Column name to check')
    parser.add_argument('--expected_mean', type=float, required=True)
    parser.add_argument('--threshold', type=float, default=0.0)
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    data = df[args.column].dropna().tolist()
    if check_mean_drift(data, args.expected_mean, args.threshold):
        print("Drift within threshold. Pipeline passes.")
        sys.exit(0)
    else:
        print("Drift beyond threshold! Pipeline fails.")
        sys.exit(1)
