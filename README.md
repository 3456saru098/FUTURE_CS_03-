# 🔐 Secure File Sharing System – FUTURE_CS_3

This is Task 3 of the **Future Interns – Cyber Security Internship 2025**, where I built a simple and secure file sharing system using Python and Flask.

It allows users to upload any file securely with **AES encryption**, and download it safely with real-time decryption — all through a clean web interface.

---

## 🚀 What This Project Does

- 📤 Uploads any type of file through a web browser  
- 🔒 Encrypts files using **AES-128 (ECB Mode)** before storing  
- 📥 Allows secure download with instant decryption  
- 🌐 Built with Flask, HTML & Python backend

---

## 🧪 How to Run This Project Locally

Make sure you have Python installed, then:

```bash
# Clone the repository (replace your-username)
git clone https://github.com/your-username/FUTURE_CS_3.git
cd FUTURE_CS_3

# Activate your virtual environment
python -m venv venv
venv\Scripts\activate   # (On Windows)

# Install required packages
pip install -r requirements.txt

# Run the app
python app.py
Now open your browser and go to:
👉 http://127.0.0.1:5000

✅ Make sure the server is running before visiting the link.

🛠 Tools & Technologies Used
Python 3

Flask (for backend)

PyCryptodome (for AES encryption)

HTML & CSS (basic frontend)

📁 Folder Overview
pgsql
Copy
Edit
FUTURE_CS_3/
├── app.py              # Main Flask app
├── encryption.py       # AES encryption & decryption logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
├── static/             # (For future styling or JS)
└── uploads/            # Encrypted files saved here
🔐 Note on Security
This project is made for educational/demo purposes only:

AES key is hardcoded (not safe in real apps)

ECB mode is used (not secure for production)

No user login system — just core encryption workflow

See encryption.py to learn how AES works in Python.

👩‍💻 Developed By
Sarita Sharma
🧑‍🎓 Intern at Future Interns Cyber Security Program
🔗 LinkedIn:https://www.linkedin.com/in/sarita-sharma-69a461308/

✅ Internship Credit
This project was completed as part of:
🎓 Future Interns – Cyber Security Internship (2025)
🔐 Task 3: Secure File Sharing System

