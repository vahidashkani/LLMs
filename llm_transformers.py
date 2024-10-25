# -*- coding: utf-8 -*-
"""LLM_Transformers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kuy7Yjq5izSvWkrrqmUbyl3ErfQAVm_8

**Notes**

This code is designed to guide users through various aspects of the Hugging Face Transformers library. Each section provides standalone functionality that demonstrates how to use transformers for NLP tasks, including simple pipelines, using custom models, and performing inference in both PyTorch and TensorFlow backends.
Requirements

    Python 3.6+
    transformers library
    torch for PyTorch sections
    tensorflow for TensorFlow sections
"""

## 2. Using the Transformers Pipeline for Sentiment Analysis

# Import the pipeline class from transformers.
from transformers import pipeline

# Initialize a sentiment-analysis pipeline. Here, we're using 'cuda' to enable GPU acceleration.
classifier = pipeline("sentiment-analysis", device='cuda')

# Run a sample text through the classifier pipeline.
result = classifier("We are happy to buy a new book.")
print("Sentiment Analysis Result:", result)

# Transformers Tutorial: Getting Started with NLP Pipelines and Model Customization

## 1. Installation
# First, install the Hugging Face Transformers library.
# This library provides pretrained models and easy-to-use NLP pipelines.

!pip install transformers

## 3. Using Tokenizer and Model Separately (PyTorch)

# Import the required modules for tokenization and model loading.
from transformers import AutoTokenizer, AutoModel

# Load a tokenizer and model directly from the Hugging Face model hub.
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Example text to tokenize and run through the model.
text = "Hello world!"

# Tokenize the text and return tensors in PyTorch format.
input_ids = tokenizer(text, return_tensors="pt")

# Run the tokenized text through the model to get the output.
output = model(**input_ids)
print("Model Output:", output)

## 4. Using TensorFlow Backend for Transformers

# Import tokenizer and model classes for TensorFlow usage.
from transformers import AutoTokenizer, TFAutoModel

# Load a tokenizer and model for TensorFlow backend.
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = TFAutoModel.from_pretrained("bert-base-uncased")

# Define a sample text for tokenization.
text = "Hello world!"

# Tokenize the text and return tensors in TensorFlow format.
input_ids = tokenizer(text, return_tensors="tf")

# Pass the tokenized input through the model.
output = model(**input_ids)
print("Model Output (TensorFlow):", output)

## 5. Custom Pipeline with Specific Tokenizer and Model

# Import necessary modules.
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Choose a specific model for sentiment analysis.
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the tokenizer and model for the chosen model.
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Initialize a pipeline with a custom model and tokenizer.
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Test the custom pipeline with sample inputs.
test_texts = [
    "We are very happy to show you the Transformers library.",
    "We hope you don't hate it."
]
results = classifier(test_texts)
for result in results:
    print("Custom Pipeline Result:", result)

## 6. Understanding Tokenizer Outputs

# Re-import modules if needed.
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Define a sample model and tokenizer.
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example text for tokenization.
text = "We are very happy to show you the Transformers library."

# Tokenize and convert tokens to IDs.
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
input_ids = tokenizer(text)

# Display the tokenized outputs.
print("Tokens:", tokens)
print("Token IDs:", token_ids)
print("Input IDs:", input_ids)

# Batch process multiple inputs with padding and truncation for sequence length consistency.
batch_input = tokenizer(
    ["We are very happy to show you the Transformers library.", "We hope you don't hate it."],
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt"
)
print("Batch Tokenization:", batch_input)

## 7. Using Tokenizer and Model Separately with PyTorch for Inference

# Import necessary libraries.
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Set up model and tokenizer.
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define input texts and prepare the batch.
texts = [
    "We are very happy to show you the Transformers library.",
    "We hope you don't hate it."
]
batch_input = tokenizer(
    texts,
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt"
)

# Disable gradient calculations for inference.
with torch.no_grad():
    outputs = model(**batch_input)

# Apply softmax to get probabilities for each class.
predictions = F.softmax(outputs.logits, dim=1)

# Determine the predicted labels by finding the index of the highest probability.
predicted_labels = torch.argmax(predictions, dim=1)

# Map label indices to human-readable labels.
labels = [model.config.id2label[label_id] for label_id in predicted_labels.tolist()]

# Display results.
print("Predicted Labels:", labels)
print("Softmax Probabilities:", predictions)

