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
- **Epochs**: *[Specify]*  
- **Batch Size**: *[Specify]*  
- **Learning Rate**: *[Specify]*  
- **Framework**: PyTorch  

Trained weights are included in the `weights` directory for replication or deployment.
