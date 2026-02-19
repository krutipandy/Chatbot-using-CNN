# Chatbot using CNN 🤖

A simple **chatbot application** built with a **Convolutional Neural Network (CNN)** that classifies user input into predefined intents and generates relevant responses. This project demonstrates how deep learning can be used for **basic conversational AI**. ([GitHub][1])

## 🔍 Features

* 💬 Text-based chatbot that responds based on intent classification
* 🧠 Uses **CNN model** for intent prediction
* 📚 Predefined intents and responses (in `intents.json`)
* 🧪 Includes training and inference code for easy experimentation 


## 🛠️ Setup & Usage

1. **Clone the repo**

   ```bash
   git clone https://github.com/krutipandy/Chatbot-using-CNN.git
   cd Chatbot-using-CNN
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**

   ```bash
   python train.py
   ```

4. **Chat with the bot**

   ```bash
   python chat.py
   ```

## 🧠 How It Works

* The chatbot reads user input and preprocesses text using NLTK utilities.
* A **CNN model** classifies this input into one of the predefined intent categories.
* Based on the predicted intent, a suitable response is selected and shown to the user. 

## 📁 File Overview

| File            | Purpose                       |
| --------------- | ----------------------------- |
| `train.py`      | Train the CNN model           |
| `chat.py`       | Run the chatbot               |
| `model.py`      | Model architecture            |
| `nltk_utils.py` | Text preprocessing helpers    |
| `intents.json`  | Intent categories & responses |
| `app.py`        | Optional web interface        |


## 🚀 Why This Project Is Useful

This project is perfect for beginners learning:

✅ NLP basics
✅ Deep learning for text classification
✅ Building AI-powered chat systems


## Generated from Youtube for understanding basis:
https://github.com/patrickloeber 
