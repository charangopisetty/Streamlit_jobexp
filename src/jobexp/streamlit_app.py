import streamlit as st
from jobexp.main import crew
#from main import crew  # ✅ correct import for sibling file
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title=" ATS Friendly Experience Generator", layout="centered")

st.title("📄 ATS Friendly Experience Generator")

st.markdown("Paste a job description below. The AI agents will craft a tailored, ATS-optimized job experience entry.")

job_description = st.text_area("Job Description", height=250)

if st.button("Generate Experience"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("⏳ Generating experience with AI agents..."):
            inputs = {'job_description': job_description}
            result = crew.kickoff(inputs=inputs)
            final_output = result.raw

        st.success("✅ Experience Generated!")

        # 🎯 ✅ Only show if final_output is defined
        st.markdown("### ✨ Final Result")

        # For bullet points
        bullets = final_output.strip().split('\n')
        for line in bullets:
            if line.strip():
                st.markdown(f"- {line.strip()}")
