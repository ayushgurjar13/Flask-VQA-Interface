# Flask-VQA-Interface

A web-based Visual Question Answering (VQA) interface built using Flask. This project allows users to upload an image, ask a question about its content, and receive an answer along with a confidence score. It leverages the power of Transformers and the `visual-question-answering` pipeline to understand and respond to queries related to the provided images.

## Features:
- **Image Upload:** Users can upload any image in standard formats (e.g., JPEG, PNG).
- **Question Submission:** Users can ask a question about the uploaded image directly through the interface.
- **AI-Powered Answers:** The app uses a pre-trained model from the Transformers library to provide accurate answers to the questions.
- **Confidence Score:** Each answer is accompanied by a confidence score, indicating the model's certainty.
- **User-Friendly Interface:** A clean and intuitive interface that makes interacting with the VQA model easy and efficient.

## Getting Started:
Clone the repository, install the required dependencies, and run the Flask app locally to start using the VQA interface.

## Dependencies:
- Flask
- Transformers
- Pillow

## Usage:
1. Upload an image.
2. Ask a question related to the image.
3. Receive an answer and confidence score from the model.

## Installation:
```bash
git clone https://github.com/yourusername/VQA-Insight.git
cd VQA-Insight
pip install -r requirements.txt
python app.py
