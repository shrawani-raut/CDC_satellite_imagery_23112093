#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install requests tqdm')


# In[5]:


import os
import requests
import pandas as pd
from tqdm import tqdm


# In[6]:


import time

def download_esri_image_safe(
    lat,
    lon,
    out_path,
    zoom=17,
    img_size=256,
    max_retries=3
):
    scale = 0.0005 * (20 - zoom)
    bbox = f"{lon-scale},{lat-scale},{lon+scale},{lat+scale}"

    url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export"

    params = {
        "bbox": bbox,
        "bboxSR": 4326,
        "imageSR": 4326,
        "size": f"{img_size},{img_size}",
        "format": "png",
        "f": "image"
    }

    for attempt in range(max_retries):
        try:
            with requests.get(
                url,
                params=params,
                stream=True,
                timeout=(10, 60)
            ) as r:
                r.raise_for_status()
                with open(out_path, "wb") as f:
                    for chunk in r.iter_content(8192):
                        if chunk:
                            f.write(chunk)
            return True

        except requests.exceptions.ReadTimeout:
            wait = 2 ** attempt
            print(f"Timeout → retrying in {wait}s")
            time.sleep(wait)

        except Exception as e:
            print("Failed:", e)
            return False

    return False


# In[ ]:


df = pd.read_csv("train(1).csv")

OUT_DIR = "/content/esri_images"
os.makedirs(OUT_DIR, exist_ok=True)

for _, row in tqdm(df.iterrows(), total=len(df)):
    img_path = f"{OUT_DIR}/{row['id']}.png"

    if os.path.exists(img_path):
        continue

    ok = download_esri_image_safe(
        lat=row["lat"],
        lon=row["long"],
        out_path=img_path,
        zoom=17,
        img_size=256
    )

    time.sleep(0.4)

    if not ok:
        print(f"Skipped ID {row['id']}")


# In[ ]:





# In[ ]:




