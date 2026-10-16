import json
import time
import streamlit as st
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"

with open("system_prompt.txt", encoding="utf-8") as f:
    SYSTEM = f.read()

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


def analyse(message, retries=3):
    for attempt in range(retries):
        try:
            reply = client.models.generate_content(
                model=MODEL,
                contents=message,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM,
                    temperature=0.2,
                    response_mime_type="application/json",
                ),
            )
            return json.loads(reply.text)
        except Exception as error:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                return {"error": str(error)}


st.set_page_config(page_title="Fake Job Offer Detector", page_icon="🕵")
st.title("🕵 Fake Job Offer Detector")
st.caption("Paste a job offer message. Do not paste real personal data.")

if "history" not in st.session_state:
    st.session_state.history = []

text = st.text_area("Job offer message", height=180)

if st.button("Check offer") and text.strip():
    with st.spinner("Checking..."):
        result = analyse(text)
    if "error" in result:
        st.error("Could not check right now. Please try again in a minute.")
    else:
        st.session_state.history.append((text[:60], result["verdict"]))
        st.subheader(f"Verdict: {result['verdict']} ({result['confidence']}%)")
        st.write("**Red flags**")
        for flag in result["red_flags"]:
            st.write(f"- {flag}")
        st.write("**What to do**")
        for step in result["what_to_do"]:
            st.write(f"- {step}")
        st.info("In India, report cyber fraud at cybercrime.gov.in or call 1930.")

if st.session_state.history:
    st.divider()
    st.write("**Checked in this session**")
    for preview, verdict in st.session_state.history:
        st.write(f"- {verdict}: {preview}...")