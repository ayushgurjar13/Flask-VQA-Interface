from flask import Flask, request, render_template
from transformers import pipeline
from PIL import Image
import os

# Initialize Flask app
app = Flask(__name__)

# Load the VQA pipeline
vqa_pipeline = pipeline("visual-question-answering")

# Ensure that the static directory exists
os.makedirs('static', exist_ok=True)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the VQA
@app.route('/vqa', methods=['POST'])
def vqa():
    if 'image' not in request.files or 'question' not in request.form:
        return "Please upload an image and provide a question.", 400

    # Get the image and question from the form
    image_file = request.files['image']
    question = request.form['question']

    # Save and open the image
    image_path = os.path.join('static', image_file.filename)
    image_file.save(image_path)
    image = Image.open(image_path).convert("RGB")  # Ensure the image is in RGB format

    # Use the VQA pipeline to get the answer
    result = vqa_pipeline(image, question, top_k=1)[0]

    # Extract the answer and confidence
    answer = result['answer']
    confidence = result['score']

    return render_template('result.html', image_url=image_path, question=question, answer=answer, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
