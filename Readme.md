# Satellite Imagery–Based Property Valuation using Multimodal Regression

The objective of this project is to predict property prices by combining **tabular housing data** with **satellite imagery** using a **multimodal regression approach**.

Unlike traditional models that rely only on numeric features, this project incorporates **visual neighborhood context** (roads, greenery, spatial layout) extracted from satellite images using a Convolutional Neural Network (CNN).

---

## Project Overview

- Predicts house prices using **tabular + satellite image data**
- Satellite images are fetched programmatically using **latitude and longitude**
- Image features are extracted using a **pretrained ResNet model**
- Tabular and image features are combined using **late fusion**
- Model explainability is demonstrated using **Grad-CAM**

---

## Dataset Description

### Tabular Dataset
- **Files**: `train(1).csv`, `test2.csv`
- **Target Variable**: `price`
- **Features include**:
  - bedrooms, bathrooms
  - sqft_living, sqft_above, sqft_basement
  - sqft_lot, sqft_living15, sqft_lot15
  - condition, grade, view, waterfront
  - latitude (`lat`), longitude (`long`)

### Visual Dataset
- **256 × 256 satellite images**
- Downloaded using **ESRI World Imagery API**
- Images represent the surrounding neighborhood of each property
  
---

## Environment Setup

### Create Environment
```bash
conda create -n multimodal python=3.9
conda activate multimodal
------

#### Install Required Libraries
pip install pandas numpy matplotlib seaborn scikit-learn
pip install torch torchvision
pip install opencv-python tqdm requests xgboost

###Download Satellite Images (Training Data)
python data_fetcher.py

### Download Satellite Images (Testing Data)
python data_fetcher_for_test_dataset.py

### Tabular Data Processing and Model Training
jupyter notebook tabular_model_final.ipynb

### Image Feature Extraction and Multimodal Fusion
jupyter notebook multimodal.ipynb

### Final Predictions are saved as:

