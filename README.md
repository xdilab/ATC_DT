# ATC_DT

![Alt text](Screenshot_2025-04-24_at_2.40.11 PM.png)

# Generation of ADSB Data

In order to create your DT csv file, you will need to first create an ADSB csv file to extract data from.

1. Ensure that the "aircraft_near_KGSO.csv" file is in the same directory as your python file, "kgso_extractor_v13.py".
2. Adjust the "csv_path" variable and the "csv_filename" accordingly to your personal directory and file name of the "adsb_hist_06_01_24_cleaned (4).csv".
3. Locate this line: "url = f"https://samples.adsbexchange.com/readsb-hist/2024/06/01/{time_str}.json.gz"" at the bottom of the kgso_extractor_v13 python file and adjust the date in the URL to your desired date for extraction.

These steps will help you create the ADSB data csv similar to the format of the "adsb_hist_06_01_24_cleaned (4).csv" shown in this repo.
