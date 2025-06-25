# 📬 AI-Powered Email Responder 🤖✉️

An intelligent email assistant that automatically reads, interprets, and responds to unread emails using a fine-tuned GPT-2 language model. Designed to mimic human-like email responses while securely integrating with Gmail using Google APIs.

---

## 🚀 Features

- 📥 Fetches unread emails using Gmail API
- 🤖 Generates contextual replies using a fine-tuned GPT-2 model (Hugging Face Transformers)
- ✉️ Sends automatic replies to real (non-no-reply) senders
- ✅ Marks emails as "read" after replying
- 🔒 Secure OAuth2 authentication with `credentials.json`
- 🧠 Skips auto-generated emails like `no-reply@google.com`, etc.
- 📌 Replies only to the latest email to avoid spamming

---

## 🧱 Project Structure

```

email\_responder/
├── main.py                      # Entry point to run the responder
├── responder.py                 # Contains the GPT-2 based response generator
├── email\_handler.py             # Handles Gmail API (fetch, send, mark read)
├── gpt2\_reply.py                # Model loading and test runner
├── gmail\_read.py                # Basic Gmail read test
├── credentials.json             # Google OAuth2 credentials
├── token.pickle                 # Stored OAuth2 token (auto-generated)
├── requirements.txt             # Python dependencies
├── training/
│   ├── dataset.csv              # Custom email-response dataset
│   └── fine\_tuning\_script.py    # (Optional) Model fine-tuning code

````

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/srivatsabaggi7/AI-Email-Responder.git
   cd email_responder
````

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gmail API credentials**

   * Go to [Google Cloud Console](https://console.cloud.google.com/)
   * Create OAuth2 credentials with Gmail API access (`readonly`, `send`)
   * Download `credentials.json` and place it in the root folder

---

## 🧠 Fine-Tuned GPT-2 Model

This project uses a fine-tuned version of **GPT-2** to generate polite, professional, and context-aware email replies. You can retrain it on your own dataset using the scripts under `training/` if desired.

---

## 🧪 How to Run

```bash
python main.py
```

* You'll be asked to authenticate via browser the first time
* The script will:

  * Fetch the latest unread email (excluding auto-generated)
  * Generate a response
  * Send it back to the sender
  * Mark that email as "read"

---

## 📁 Dataset Sample (for GPT-2 Training)

| email\_text                                     | response\_text                                   |
| ----------------------------------------------- | ------------------------------------------------ |
| Could you please share the report by EOD?       | Sure! I’ll send it to you before the end of day. |
| Let me know your availability for a quick call. | I'm available post 3 PM today. Does that work?   |

---



## 🙌 Credits

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [Google Gmail API](https://developers.google.com/gmail/api)
* [OpenAI GPT-2 Model](https://github.com/openai/gpt-2)

---

## 🧠 Author

Srivatsa V Baggi (https://github.com/srivatsabaggi7)

```
