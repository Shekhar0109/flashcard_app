# Flashcard App 📚

This is a simple Streamlit web app that generates flashcards from text using natural language processing (NLP) with Hugging Face Transformers.

## 🚀 Features

- Input custom text (or load from file if enabled)
- Automatically generates flashcards (Q&A style)
- Clean, user-friendly interface using Streamlit

## 🔧 Tech Stack

- Python 🐍
- Streamlit
- Hugging Face Transformers
- (Optionally) PDF parsing with `pdfminer.six`

## 🛠 Installation


# Clone the repository
git clone https://github.com/Shekhar0109/flashcard_app.git
cd flashcard_app

# Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
If requirements.txt is not created yet, use this:


pip install streamlit transformers
pip freeze > requirements.txt
▶️ Run the App

streamlit run app.py
It will open in your browser at http://localhost:8501

📝 Usage
Enter the text you want to convert into flashcards.

Click the Generate button.

Review your generated flashcards instantly.

💡 Future Ideas:-
  PDF or DOCX input support
 
  Export flashcards to CSV or Anki format
 
  UI improvements

🧑‍💻 Author
Made with ❤️ by Shekhar0109
![Screenshot 2025-06-14 003928](https://github.com/user-attachments/assets/1b01160f-ad60-4d76-a489-f8a457daa2e7)

