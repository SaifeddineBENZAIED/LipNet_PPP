# Lip Reading with Deep Learning

This repository contains a **Deep Learning model** capable of interpreting lip movements to convert videos into text. The project is designed for applications in **accessibility** and **communication**, providing a tool to assist individuals with hearing impairments or to enhance communication in noisy environments.

The repository also includes a **Streamlit app** that allows users to test the model on their own videos, making it easy to visualize and interact with the project.

---

## 🚀 Features

- **Deep Learning Model**: Built with **TensorFlow** and **OpenCV**, the model uses a **3D Convolutional Neural Network (CNN)** combined with **Bidirectional LSTM** layers to interpret lip movements.
- **Streamlit App**: A user-friendly interface to upload videos and see the model's predictions in real-time.
- **Accessibility**: Designed to assist individuals with hearing impairments or enhance communication in challenging environments.
- **Pre-trained Models**: Includes pre-trained checkpoints for quick deployment and testing.

---

## 🛠️ Technologies Used

- **Deep Learning Framework**: TensorFlow
- **Computer Vision**: OpenCV
- **Web App Framework**: Streamlit
- **Data Processing**: NumPy, Pandas
- **Model Training**: Keras, CTC Loss

---

## 📂 Repository Structure

LipNet_PPP/

├── app/ # Streamlit app for testing the model

│ ├── main.py # Streamlit application code

│ └── requirements.txt # Dependencies for the Streamlit app

├── models/ # Pre-trained model checkpoints

│ ├── checkpoint_50/ # Model checkpoint at epoch 50

│ └── checkpoint_96/ # Model checkpoint at epoch 96

├── data/ # Dataset and alignment files

│ ├── alignments/ # Alignment files for training

│ └── videos/ # Sample videos for testing

├── README.md # Project documentation

└── .gitignore # Git ignore file


---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- TensorFlow 2.x
- Streamlit
- OpenCV

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SaifeddineBENZAIED/lip-reading-deep-learning.git
   cd lip-reading-deep-learning
Install Dependencies:

```bash
pip install -r app/requirements.txt
```

Run the Streamlit App:

```bash
streamlit run app/main.py
```

The app will be available at http://localhost:8501.

Test the Model:

- Upload a video file through the Streamlit interface.

- The app will process the video and display the predicted text.

🔍 Key Features

Deep Learning Model

- 3D CNN + Bidirectional LSTM: The model architecture combines 3D convolutional layers for spatial-temporal feature extraction and bidirectional LSTM layers for sequence modeling.

- CTC Loss: Used for training the model to align video frames with text predictions.

- Pre-trained Checkpoints: Includes checkpoints at different training epochs for quick testing.

Streamlit App

- User-Friendly Interface: Allows users to upload videos and view predictions.

- Real-Time Processing: Processes videos and displays results in real-time.

- Accessibility: Designed to be intuitive and easy to use.

📫 Contact
For questions or feedback, feel free to reach out:

- Email: saif2001benz2036@gmail.com
