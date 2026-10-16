
# Fake Job Offer Detector

A web app that checks a pasted job offer (from SMS, WhatsApp, email or LinkedIn) and says whether it is **FAKE**, **SUSPICIOUS** or **GENUINE**. It returns a confidence score, the red flags it found, and what the user should do next.

**Live demo:** [add your Streamlit link here]

## Why this project
Fake job offers that ask for registration fees or personal documents are common in India, and freshers are often the targets. This tool gives a quick first check before a user pays money or shares Aadhaar, PAN or bank details.

## How it works
1. The user pastes a job offer message.
2. The Streamlit app sends it to the Gemini API with a fraud-analyst system prompt.
3. The model replies in JSON: verdict, confidence, red flags and action steps.
4. The app shows the result in a simple format.

## Red flags checked
- Registration or training fees
- Personal email domains (Gmail, Yahoo) instead of a company domain
- Unrealistic salary for the role
- No interview process
- WhatsApp or Telegram-only contact
- Urgency and pressure
- Requests for Aadhaar, PAN or bank details

## Tech stack
- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Pandas (evaluation)

## Evaluation
Tested on [40] made-up messages ([18] fake, [14] genuine, [8] tricky).

| Version | Accuracy |
|---|---|
| Initial prompt | [__]% |
| Improved prompt (with examples) | [__]% |

The confusion matrix is in `results.csv` and in the report screenshots.

## Run it locally
1. Clone the repo and open the folder.
2. Install the packages:
   ```
   pip install -r requirements.txt
   ```
3. Create `.streamlit/secrets.toml` with your free Gemini API key from aistudio.google.com:
   ```
   GEMINI_API_KEY = "your-key-here"
   ```
4. Run the app:
   ```
   python -m streamlit run app.py
   ```

## Project files
- `app.py` is the Streamlit app
- `system_prompt.txt` is the fraud-analyst prompt
- `tests.csv` holds the labelled test messages
- `evaluate.py` measures accuracy and the confusion matrix
- `requirements.txt` lists the dependencies

## Limitations
- It can miss new scam styles it hasn't seen.
- It works only from the text pasted in. It cannot verify a company, a domain or a phone number.
- It is a first-check aid, not proof. Always confirm an offer on the company's official website or careers page.
- Free-tier API limits apply, and prompts on the free tier may be used by Google to improve its products, so use only sample or made-up messages.
