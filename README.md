# **AI-Driven Defect Detection for Automotive Manufacturing**

## **Overview**
This project is an AI-powered defect detection system designed to enhance quality control in automotive manufacturing. By leveraging advanced machine learning and computer vision techniques, the solution automates defect identification, classifies defects, and provides actionable insights to address quality issues.

## **Key Features**
- **Automated Defect Identification**: Analyze uploaded images to detect and classify defects in automotive parts.
- **Comprehensive Defect Reports**: Includes the defect type, causes, and recommended solutions.
- **Intuitive Web Interface**: User-friendly design for seamless interaction.
- **Real-Time Processing**: Rapid analysis for faster decision-making.
- **Actionable Insights**: Provides strategies to mitigate identified defects.

## **System Architecture**
1. **User Input**: Upload an image of an automotive part.
2. **Backend Processing**:
   - Image data is processed using the **Google Gemini API** for defect classification.
   - Defect type, cause, and recommendations are retrieved.
3. **Response Display**: The system displays a detailed defect report on an interactive UI.



## **Tech Stack**
### **Frontend**
- HTML5, CSS3, JavaScript
- Bootstrap for responsive design
- Interactive animations and dynamic UI elements

### **Backend**
- Flask (Python)
- Google Gemini API for defect classification
- PIL (Python Imaging Library) for image processing

### **Development Tools**
- Visual Studio Code
- GitHub for version control
- Google Colab for model testing

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name

2. Run the application:
    ```bash
    python app.py

## **Usage**

1. Open the web application at http://localhost:5000.
2. Upload an image of an automotive part.
3. Enter the part name and submit.
4. View the detailed defect report, including defect type, causes, and solutions.

## **File Structure**
     
    ├── static/
    │   ├── css/                # Custom CSS files
    │   ├── images/             # Images used in the project
    │   └── js/                 # JavaScript files
    ├── templates/
    │   ├── index.html          # Homepage
    │   ├── result.html         # Results page
    ├── app.py                  # Flask application
    ├── requirements.txt        # Dependencies
    ├── .env                    # Environment variables
    └── README.md               # Project documentation
      
## **Future Enhancements**
1. Expand defect classification categories.
2. Integrate with IoT sensors for real-time inspection.
3. Add multi-language support for global usability.
