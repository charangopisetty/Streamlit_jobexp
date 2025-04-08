import streamlit as st
from jobexp.main import crew
from dotenv import load_dotenv
import streamlit.components.v1 as components

load_dotenv()

st.set_page_config(page_title="ATS Friendly Experience Generator", layout="centered")

st.title("📄 ATS Friendly Experience Generator")

st.markdown("Paste a job description below. The AI agents will craft a tailored, ATS-optimized job experience entry.")

# === User Inputs ===
job_description = st.text_area("Job Description", height=250)
role = st.text_input("What role is this for?")
bullet_range = st.selectbox("Number of Bullet Points", ["1-2", "2-4", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"], index=2)
tone = st.selectbox("Tone", ["Technical", "Leadership", "Cross-functional", "Creative"])

# === Generate Button Logic ===
if st.button("🚀 Generate Experience"):
    if not job_description.strip() or not role.strip():
        st.warning("❗ Please enter both the job description and the target role.")
    else:
        with st.spinner("⏳ Generating experience with AI agents..."):
            inputs = {
                'job_description': job_description,
                'role': role,
                'bullet_range': bullet_range,
                'tone': tone
            }
            result = crew.kickoff(inputs=inputs)
            final_output = result.raw

        st.success("✅ Experience Generated!")
        st.markdown("### ✨ Final Result")

        # === Copy Button HTML ===
        copy_button_html = f"""
            <textarea id="copyTarget" style="position: absolute; left: -9999px;">{final_output}</textarea>
            <button onclick="copyToClipboard()" style="
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 5px;
                cursor: pointer;
                margin-bottom: 10px;
            ">📋 Copy Experience</button>
            <script>
            function copyToClipboard() {{
                var copyText = document.getElementById("copyTarget");
                copyText.select();
                document.execCommand("copy");
                alert("Copied to clipboard!");
            }}
            </script>
        """
        components.html(copy_button_html, height=60)

        # === Display as Bullet Points ===
        bullets = final_output.strip().splitlines()
        for line in bullets:
            if line.strip():
                st.markdown(f"- {line.strip()}")
