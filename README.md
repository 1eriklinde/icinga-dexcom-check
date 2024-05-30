<img width="291" alt="image" src="https://github.com/1eriklinde/icinga-dexcom-check/assets/108029729/d3ccf913-21fb-4cd3-ba22-10f01c821491">


Icinga plugin to monitor Dexcom bloodsugar values in Icinga (https://github.com/Icinga/icinga2)

Requires Pydexcom (https://github.com/gagebenne/pydexcom)

**Note:** Set up environmental variables for your Dexcom username and password to avoid having them in plaintext:

export DEXCOM_USER=YOURDEXCOMUSERNAME<br>
export DEXCOM_PASSWORD=YOURDEXCOMPASSWORD


**Thresholds for blood sugar levels in mmol/L:**

  LOW_CRITICAL_THRESHOLD = 3.0
  
  LOW_WARNING_THRESHOLD = 4.0
  
  HIGH_WARNING_THRESHOLD = 11.0
  
  HIGH_CRITICAL_THRESHOLD = 15.0
