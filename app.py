import streamlit as st
from ultralytics import YOLO
import pandas as pd
from PIL import Image
import numpy as np
import tempfile
import os
import shutil

PATH = os.path.dirname(__file__)
model = YOLO(PATH + "/Model/weights/last.pt")

def detect_fractures(image_path, save_dir, image_name):
    results = model(image_path, save=True, save_dir=save_dir, name=image_name, show_labels=False)
    return results

st.title("Kidney Stone Detection Model")
st.write("Upload a medical image (MRI/CT Scan) of a kidney.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)
    st.write("Detecting Kidney Stone...")

    image_np = np.array(image)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmpfile:
        image_pil = Image.fromarray(image_np)
        image_pil.save(tmpfile.name)
        tmpfile_path = tmpfile.name

    image_name = os.path.splitext(uploaded_file.name)[0]

    save_dir = os.path.join('yolov8_predictions', image_name)
    os.makedirs(save_dir, exist_ok=True)

    results = detect_fractures(tmpfile_path, save_dir, image_name)
    
    shutil.rmtree('yolov8_predictions')
    os.unlink(tmpfile_path)

    predictions_data = []

    for result in results:
        boxes = result.boxes
        names = result.names

        for i, box in enumerate(boxes):
            class_name = names[int(box.cls.item())]
            confidence = box.conf.item() if box.conf is not None else 0.0
            x_center, y_center, width, height = box.xywh[0]

            predictions_data.append({
                "Class": class_name,
                "Confidence": f"{(round(confidence, 2)*100)}%",
                "X Center": round(x_center.item(), 2),
                "Y Center": round(y_center.item(), 2),
                "Width": round(width.item(), 2),
                "Height": round(height.item(), 2)
            })

    if predictions_data:
        df = pd.DataFrame(predictions_data)
        st.dataframe(df)

        for info in results:
            predict_dir = info.save_dir

        if os.path.exists(predict_dir) and os.listdir(predict_dir):
            image_name = os.listdir(predict_dir)
            image_prediction = os.path.join(predict_dir, image_name[0])

            st.image(image_prediction, caption="Processed Image", use_container_width=True)
            shutil.rmtree('runs')
            st.write("Diagnostic completed ✅")
    
    else:
        st.write("No Kidney Stones found")
        print("No prediction results found [No Kidney Stone found]")
