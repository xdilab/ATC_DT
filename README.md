# ATC_DT

![Alt text](Screenshot_2025-04-24_at_2.40.11 PM.png)

# Step 1: Install Dependencies

In the "kgso_extractor_v13.py" python file, which in the generation of ADSB data, you will need to use the following libraries:
```python
import gzip
import requests
from math import radians, sin, cos, sqrt, atan2
import json
import csv
```

You will need to install the packages for each library. Here is a list of necessary commands for installation:
<pre>
!pip install requests
!pip install gzip
!pip install json
</pre>

Similarly, you will need to use the following libraries in the "ATC_SIM_v_main.ipynb" python file, which is used to create your Digital Twin(DT) data and ATC visualization:

```python
import pandas as pd
import numpy as np
import time as tm
import csv
from datetime import datetime, timedelta, time
import os
from collections import Counter
import json
import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.transforms import Affine2D
from scipy.ndimage import rotate
from shapely.geometry import LineString
```

Here is a command listing the necessary packages for installation:

<pre> !pip install pandas numpy matplotlib contextily geopandas shapely scipy </pre>

# Step 2: Generation of ADSB Data

In order to create your DT csv file, you will need to first create an ADSB csv file to extract data from.

1. "readsb-hist" is an online histoircal data source that is used to extract a full CSV containing ATC data from multiple dates and times. The objective of the "kgso_extractor_v13.py" script is to extract specific date and time segments of this CSV, creating the ADSB data generated in this step. We will be extracting from the "aircraft_near_KGSO.csv" file located in this github.
   
2. Ensure that the "aircraft_near_KGSO.csv" file is in the same directory as your python file, "kgso_extractor_v13.py".

3. In the python file, adjust the "csv_path" variable and the "csv_filename" accordingly to your personal directory and file name of the "adsb_hist_06_01_24_cleaned (4).csv".

4. Locate this line: "url = f"https://samples.adsbexchange.com/readsb-hist/2024/06/01/{time_str}.json.gz"" at the bottom of the kgso_extractor_v13 python file and adjust the date in the URL to your desired date for extraction.

These steps will help you create the ADSB data csv similar to the format of the "adsb_hist_06_01_24_cleaned.csv" shown in this repo.

# Step 3: Generation of DT Visualization and CSV Data

Once you have the ADSB data csv, you can move on to generating the aircraft visualization and DT CSV data.

1. Ensure that these files are all in the same directory: new_freq_filesWAV2TXT - KGSO_ATIS 2_reformatted_with_final_times_VID.csv, new_freq_filesWAV2TXT - KGSO_Approach_Departure 2_reformatted_with_final_times_VID.csv, new_freq_filesWAV2TXT - KGSO_TOWER 2_reformatted_with_final_times_VID.csv, synthetic.json, ATC_SIM_v_main.ipynb, and your ADSB CSV.
   
2. In the "ATC_SIM_v_main.ipynb" python file, locate the transcription file list and adjust the files paths based on your own directory:
   ```python
   transcription_files = [
        '/Users/naimbaker/Documents/ATC/new_freq_filesWAV2TXT - KGSO_ATIS 2_reformatted_with_final_times_VID.csv',
        '/Users/naimbaker/Documents/ATC/new_freq_filesWAV2TXT - KGSO_Approach_Departure 2_reformatted_with_final_times_VID.csv',
        '/Users/naimbaker/Documents/ATC/new_freq_filesWAV2TXT - KGSO_TOWER 2_reformatted_with_final_times_VID.csv'
    ]
    ```
    
3. Locate the "csv_file" variable a few lines below the transcription file list and adjust it to the path of your ADSB CSV.

4. Locate the "output_path" variable and adjust to the directory you are working in.

5. Create a folder called "ATC Aircraft Maps" in the same directory.

Your file setup is now complete. Run your DT code and follow the directions of the text entries to create your visualization and DT data response.
