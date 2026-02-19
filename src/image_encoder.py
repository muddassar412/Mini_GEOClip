# src/image_encoder.py

import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image


class ImageEncoder:
    def __init__(self, model_name="openai/clip-vit-base-patch32", device=None):
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = CLIPModel.from_pretrained(model_name).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(model_name)

    def encode_images(self, image_paths):
        images = [Image.open(p).convert("RGB") for p in image_paths]

        inputs = self.processor(images=images, return_tensors="pt", padding=True)

        pixel_values = inputs["pixel_values"].to(self.device)

        with torch.no_grad():
            image_features = self.model.get_image_features(pixel_values=pixel_values)

        image_features = image_features / image_features.norm(dim=-1, keepdim=True)

        return image_features