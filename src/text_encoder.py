# src/text_encoder.py

import torch
from transformers import CLIPProcessor, CLIPModel


class TextEncoder:
    def __init__(self, model_name="openai/clip-vit-base-patch32", device=None):
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = CLIPModel.from_pretrained(model_name).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(model_name)

    def encode_texts(self, class_names):
        prompts = [f"a satellite image of a {cls}" for cls in class_names]

        inputs = self.processor(text=prompts, return_tensors="pt", padding=True)

        input_ids = inputs["input_ids"].to(self.device)
        attention_mask = inputs["attention_mask"].to(self.device)

        with torch.no_grad():
            text_features = self.model.get_text_features(
                input_ids=input_ids,
                attention_mask=attention_mask
            )

        text_features = text_features / text_features.norm(dim=-1, keepdim=True)

        return text_features