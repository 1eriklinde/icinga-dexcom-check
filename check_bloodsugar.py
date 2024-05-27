#!/usr/bin/env python3

import sys
from pydexcom import Dexcom

# Replace with your Dexcom credentials
DEXCOM_USER = "YOURDEXCOMUSERNAME"
DEXCOM_PASSWORD = "YOURDEXCOMPASSWORD"

# Thresholds for blood sugar levels in mmol/L
LOW_WARNING_THRESHOLD = 4.0
LOW_CRITICAL_THRESHOLD = 3.0
HIGH_WARNING_THRESHOLD = 11.0
HIGH_CRITICAL_THRESHOLD = 15.0

def main():
    try:
        dexcom = Dexcom(DEXCOM_USER, DEXCOM_PASSWORD, ous=True)
        bg = dexcom.get_current_glucose_reading()
        bg_value = bg.mmol_l

        if bg_value is None:
            print("UNKNOWN - No blood sugar reading available")
            sys.exit(3)

        if bg_value < LOW_CRITICAL_THRESHOLD:
            print(f"CRITICAL - Blood sugar is too low: {bg_value} mmol/L")
            sys.exit(2)
        elif bg_value < LOW_WARNING_THRESHOLD:
            print(f"WARNING - Blood sugar is low: {bg_value} mmol/L")
            sys.exit(1)
        elif bg_value > HIGH_CRITICAL_THRESHOLD:
            print(f"CRITICAL - Blood sugar is too high: {bg_value} mmol/L")
            sys.exit(2)
        elif bg_value > HIGH_WARNING_THRESHOLD:
            print(f"WARNING - Blood sugar is high: {bg_value} mmol/L")
            sys.exit(1)
        else:
            print(f"OK - Blood sugar is normal: {bg_value} mmol/L")
            sys.exit(0)

    except Exception as e:
        print(f"UNKNOWN - Error occurred: {str(e)}")
        sys.exit(3)

if __name__ == "__main__":
    main()