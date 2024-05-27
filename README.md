# icinga-dexcom-check
Icinga plugin to monitor Dexcom bloodsugar values in icinga

Requires Pydexcom set up (https://github.com/gagebenne/pydexcom)


# Thresholds for blood sugar levels in mmol/L
LOW_WARNING_THRESHOLD = 4.0
LOW_CRITICAL_THRESHOLD = 3.0
HIGH_WARNING_THRESHOLD = 11.0
HIGH_CRITICAL_THRESHOLD = 15.0
