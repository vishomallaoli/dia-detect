# 🎯 DiaDetect - Your Personal Diabetes Risk Predictor 🩺

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-v2.0.1-orange)](https://flask.palletsprojects.com/)
[![Model](https://img.shields.io/badge/Model-SVM-brightgreen)](https://scikit-learn.org/stable/modules/svm.html)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-7952B3)](https://getbootstrap.com/)

**DiaDetect** is a sleek and functional web application designed to help users assess their risk of diabetes based on health metrics. Powered by **Machine Learning** and a simple, user-friendly **Flask** interface, it leverages a Support Vector Machine (SVM) model to predict diabetes likelihood. Just fill in your basic health parameters, and DiaDetect will analyze your risk of diabetes in an instant.

![App Screenshot](screenshot.png)

---

## 🚀 Features
- 🧮 **Machine Learning**: Trained Support Vector Machine (SVM) model for accurate predictions.
- 🧑‍⚕️ **Health Metrics**: Input health data like BMI, glucose level, and more to assess diabetes risk.
- ⚡ **Fast and Lightweight**: Built using Flask, the app is fast and responsive.
- 🎨 **Beautiful UI**: A modern, mobile-responsive design powered by Bootstrap 4.
- 🔍 **Explainability**: Simple results that are easy to interpret for users with or without medical knowledge.

---

## 📸 Screenshots & Demos

### 🖼️ Screenshot - Input Form
![Input Form](assets/input-form.png)

### 🖼️ Screenshot - Prediction Result
![Prediction Result](assets/prediction-result.png)

### 🎬 GIF Demo
![App in Action](assets/app-demo.gif)

---

## 🛠️ Technologies Used

| Technology        | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| **Python**        | Core programming language for backend logic and machine learning. |
| **Flask**         | Lightweight web framework used to serve the application.          |
| **Scikit-learn**  | Python library for implementing the Support Vector Machine (SVM). |
| **Bootstrap 4**   | Frontend framework for responsive design and UI components.       |
| **Joblib**        | Used for saving and loading the trained machine learning model.   |
| **HTML/CSS**      | Structure and design of the web interface.                        |

---

## 📊 Machine Learning Model

The diabetes prediction model is built using a **Support Vector Machine (SVM)**. The following health metrics are used as features for prediction:

1. **Pregnancies**: Number of pregnancies.
2. **Glucose**: Plasma glucose concentration.
3. **Blood Pressure**: Diastolic blood pressure in mm Hg.
4. **Skin Thickness**: Triceps skinfold thickness in mm.
5. **Insulin**: 2-Hour serum insulin level (mu U/ml).
6. **BMI**: Body mass index (weight in kg/(height in m)^2).
7. **Diabetes Pedigree Function**: A function that scores the likelihood of diabetes based on family history.
8. **Age**: The age of the individual.

The model was trained using the **Pima Indians Diabetes Database** from the UCI Machine Learning Repository.

---

## 🎨 User Interface

DiaDetect features a clean and modern interface, designed with **Bootstrap 4**. It’s mobile-friendly, ensuring users can interact with the app on any device.

- The form is straightforward, with health inputs clearly labeled.
- The prediction result is displayed in a friendly and informative format.

---

## ⚙️ Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vishomallaoli/dia-detect.git
   cd dia-detect
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   flask run
   ```

5. Open your browser and go to `http://127.0.0.1:5000/`.

---

## 🧪 How to Use

1. Open the DiaDetect web interface.
2. Enter your health metrics such as **Glucose**, **BMI**, and **Age**.
3. Hit the "Predict" button.
4. The app will instantly display whether you're at risk for diabetes based on the input.

---

## 📂 Project Structure

```plaintext
📁 dia-detect/
│
├── 📁 templates/          # HTML templates
│   └── index.html         # Main page for user input and result
│
├── app.py                 # Main Flask application
├── svm_model_8_features.joblib  # Pre-trained SVM model file
├── requirements.txt       # Python dependencies
├── README.md              # Project README (this file)
└── .gitignore             # Ignored files and directories
```

---

## 👥 Contributors

- **Visho Malla Oli** - Project Lead & Developer  
[GitHub Profile](https://github.com/vishomallaoli)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🛠️ Future Enhancements

- **More Features**: Incorporate additional health metrics to improve accuracy.
- **Graphical Output**: Display risk results with visual aids like charts or graphs.
- **User Accounts**: Allow users to save and track their predictions over time.

---

## 🌟 Show Your Support

If you found this project helpful, consider giving it a ⭐️ on GitHub!

```

### Key Components:

1. **Fancy Design Elements**:
   - Badge icons for technologies used, model type, and license.
   - Eye-catching section titles with emojis.
   
2. **Functional and Descriptive**:
   - Clearly explains the purpose and features of the project.
   - Technologies are broken down and explained in a concise table.
   - Provides instructions on installation, usage, and future enhancements.

3. **Visual and User-Friendly**:
   - Includes a section for future improvements, which encourages contributions and feedback.
   - Describes each component of the project, from technologies used to how the app works.
