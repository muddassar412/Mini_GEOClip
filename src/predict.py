# src/predict.py

import os
from sklearn.metrics import accuracy_score
from src.image_encoder import ImageEncoder
from src.text_encoder import TextEncoder
from src.similarity import compute_similarity, predict_classes


def load_dataset(data_dir):
    image_paths = []
    labels = []

    class_names = sorted(os.listdir(data_dir))

    for cls in class_names:
        cls_folder = os.path.join(data_dir, cls)
        for img_name in os.listdir(cls_folder):
            image_paths.append(os.path.join(cls_folder, img_name))
            labels.append(cls)

    return image_paths, labels, class_names


def run_prediction(data_dir):
    image_paths, true_labels, class_names = load_dataset(data_dir)

    image_encoder = ImageEncoder()
    text_encoder = TextEncoder()

    image_features = image_encoder.encode_images(image_paths)
    text_features = text_encoder.encode_texts(class_names)

    similarity_matrix = compute_similarity(image_features, text_features)
    predicted_labels = predict_classes(similarity_matrix, class_names)

    accuracy = accuracy_score(true_labels, predicted_labels)

    return accuracy, predicted_labels, true_labels