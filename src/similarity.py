# src/similarity.py

import torch


def compute_similarity(image_features, text_features):
    """
    Computes cosine similarity between image and text embeddings
    """
    similarity = image_features @ text_features.T
    return similarity


def predict_classes(similarity_matrix, class_names):
    """
    Returns predicted class names
    """
    probs = similarity_matrix.softmax(dim=-1)
    preds = probs.argmax(dim=-1)

    predicted_labels = [class_names[idx] for idx in preds.cpu().numpy()]
    return predicted_labels