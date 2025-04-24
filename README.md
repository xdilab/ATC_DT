# ATC_DT

![Alt text](Screenshot_2025-04-24_at_2.40.11 PM.png)

# Generation of ADSB Data

In order to create your DT csv file, you will need to first create an ADSB csv file to extract data from.

1. Ensure that the "aircraft_near_KGSO.csv" file is in the same directory as your python file, "kgso_extractor_v13.py".
2. In the python file, adjust the "csv_path" variable and the "csv_filename" accordingly to your personal directory and file name of the "adsb_hist_06_01_24_cleaned (4).csv".
3. Locate this line: "url = f"https://samples.adsbexchange.com/readsb-hist/2024/06/01/{time_str}.json.gz"" at the bottom of the kgso_extractor_v13 python file and adjust the date in the URL to your desired date for extraction.

These steps will help you create the ADSB data csv similar to the format of the "adsb_hist_06_01_24_cleaned (4).csv" shown in this repo.

# Generation of DT Visualization and CSV Data

Once you have the ADSB data csv, you can move on to generating the aircraft visualization and DT CSV data.

1. Ensure that these files are all in the same directory: KGSO_ATIS 2_reformatted_with_final_times_VID.csv, KGSO_Approach_Departure 2_reformatted_with_final_times_VID.csv, KGSO_TOWER 2_reformatted_with_final_times_VID.csv, synthetic.json, ATC_SIM_v_main.ipynb, and your ADSB CSV.
2. In the "ATC_SIM_v_main.ipynb" python file, locate the transcription file list and adjust the files paths based on your own directory: transcription_files = [
        '/Users/naimbaker/Documents/ATC/new_freq_filesWAV2TXT - KGSO_ATIS 2_reformatted_with_final_times_VID.csv',
        '/Users/naimbaker/Documents/ATC/new_freq_filesWAV2TXT - KGSO_Approach_Departure 2_reformatted_with_final_times_VID.csv',
        '/Users/naimbaker/Documents/ATC/new_freq_filesWAV2TXT - KGSO_TOWER 2_reformatted_with_final_times_VID.csv'
    ]
3. Locate the "csv_file" variable a few lines below the transcription file list and adjust it to the path of your ADSB CSV.
4. Locate the "output_path" variable and adjust to the directory you are working in.
5. Create a folder called "ATC Aircraft Maps" in the same directory.

Your file setup is now complete. Run your DT code and follow the directions of the text entries to create your visualization and DT data response.
