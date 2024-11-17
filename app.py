from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import base64

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key="YOUR GOOGLE API KEY")

# Initialize Flask app
app = Flask(__name__)

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt, image[0]])
    return response.text

# Function to handle uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        image_parts = [
            {
                "mime_type": uploaded_file.content_type,
                "data": bytes_data
            }
        ]
        # Save uploaded image temporarily to display it
        image_path = os.path.join("static", "uploaded_image.jpg")
        with open(image_path, "wb") as img_file:
            img_file.write(bytes_data)
        return image_parts, image_path
    else:
        raise FileNotFoundError("No file uploaded")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_defect', methods=['POST'])
def check_defect():
    uploaded_file = request.files['image']  # Use the correct form field name from your HTML
    input_prompt = """
    You are an automotive quality inspection expert. Analyze the automotive part in the provided image and identify any defects.
    Provide a detailed report on the observed defects and potential remedies or suggestions for fixing the defects.
    Provide the report in the following format:

    Name of the part
    Defect Name: Name of the defect (e.g., Scratch, Dent, etc.)
    Cause of Defect: Description of what caused the defect
    Reason: Description of how the defect appears (e.g., location, size, shape, etc.)
    Conditions Favoring Defect: Environmental or handling conditions that may lead to the defect
    Solution: Description of how to fix or address the defect
    Additional Information: Any other relevant details
    """

    if uploaded_file:
        try:
            # Process the image data and get the response from the Gemini API
            image_data, image_path = input_image_setup(uploaded_file)
            response_text = get_gemini_response(input_prompt, image_data)
            formatted_response = format_response(response_text)
            
            # Render the response directly on index.html
            return render_template('result.html', response=formatted_response, image_path=image_path)
        except FileNotFoundError:
            return render_template('index.html', error="No file uploaded"), 400
        except Exception as e:
            return render_template('index.html', error=str(e)), 500

    # Redirect to index if no file is uploaded
    return redirect(url_for('index'))
# Function to format response into structured HTML without asterisks
def format_response(response_text):
    # Remove any "***" from response
    cleaned_text = response_text.replace("***", "")
    sections = cleaned_text.split("\n")
    formatted = "<br>".join(sections)
    return formatted

if __name__ == '__main__':
    app.run(debug=True)
