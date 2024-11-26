# UroVision: AI-Based Kidney Stone Detection System  

**UroVision** is an advanced deep learning-based system designed to detect kidney stones from medical images. Built using the **YOLOv8n** object detection model and deployed with **Streamlit**, this project aims to provide an efficient, real-time diagnostic tool for healthcare professionals.

**Link:** https://urovision.streamlit.app/
---

## Table of Contents  
- [Introduction](#introduction)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Model Architecture](#model-architecture)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results](#results)  
- [Challenges and Future Work](#challenges-and-future-work)  
- [Contributors](#contributors)  

---

## Introduction  
Kidney stone diagnosis often relies on manual examination of medical imaging, which can be time-consuming and error-prone. **UroVision** automates this process using state-of-the-art AI techniques, offering:  
- High detection accuracy.  
- Real-time prediction via an interactive web interface.  
- A scalable, easy-to-deploy solution.

---

## Features  
- **Efficient Object Detection**: Utilizes **YOLOv8n**, a lightweight yet powerful object detection model.  
- **Interactive Deployment**: Built with **Streamlit**, allowing easy image uploads and real-time visualization of results.  
- **Scalability**: Model optimized for deployment in clinical or cloud environments.

---

## Dataset  
The model is trained on a dataset sourced from [Roboflow](https://universe.roboflow.com/forsuccess/kidneydetection-k9dju), consisting of annotated images of kidney stones.  
- **Training Data**: 80% of the dataset.  
- **Validation Data**: 20% of the dataset.

---

## Model Architecture  
**YOLOv8n** is chosen for its balance between performance and computational efficiency. The model was trained with the following parameters:  
- **Epochs**: *32*  
- **Batch Size**: *32*  
- **Learning Rate**: *0.001*  
- **Framework**: Ultralytics (YOLO)  

Trained weights are included in the `weights` directory for replication or deployment.

---

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/mohitmahajan095/UroVision_-Kidney_Stone_Dection_System-.git
   cd UroVision_-Kidney_Stone_Dection_System-
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:
   ```bash
   streamlit run app.py

---
## Usage
1. Launch the Streamlit app.
2. Upload an ultrasound image via the interface.
3. View the detected kidney stones with bounding boxes and confidence scores.

---

## Results
The system achieved the following metrics on the validation dataset:

Precision: 84.4%
Recall: 70.3%
F1-Score: 0.77 at 0.378
Visual outputs:

Precision-Recall Curve
![PR-Curve](https://github.com/mohitmahajan095/UroVision_-Kidney_Stone_Dection_System-/blob/main/Model/PR_curve.png?raw=true)

F1-Score Curve
![F1-Score Curve](https://github.com/mohitmahajan095/UroVision_-Kidney_Stone_Dection_System-/blob/main/Model/F1_curve.png?raw=true)

Confusion Matrix
![Confusion Matrix](https://github.com/mohitmahajan095/UroVision_-Kidney_Stone_Dection_System-/blob/main/Model/confusion_matrix.png?raw=true)

Sample Predictions:
   val_labels:
   ![True Labels & Bounding Boxes](https://github.com/mohitmahajan095/UroVision_-Kidney_Stone_Dection_System-/blob/main/Model/val_batch1_labels.jpg?raw=true)
   
   val_prediction:
   ![Predicted Labels & Bounding Boxes](https://github.com/mohitmahajan095/UroVision_-Kidney_Stone_Dection_System-/blob/main/Model/val_batch1_pred.jpg?raw=true)
   
