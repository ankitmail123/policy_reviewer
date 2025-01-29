import streamlit as st
import openai
from dotenv import load_dotenv
import os
import PyPDF2
from docx import Document
import io

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def analyze_policy_compliance(document_text, standard_name, controls_description):
    prompt = f"""
    You are a policy compliance expert. Analyze the following policy document against the given security standard and controls.
    
    Policy Document:
    {document_text}
    
    Standard Name: {standard_name}
    Controls Description: {controls_description}
    
    Please analyze if the policy complies with the given controls. For each control:
    1. State if it complies (Yes/No)
    2. If it complies, quote the exact text from the document that demonstrates compliance
    3. If it doesn't comply, explain the gap and provide specific text that should be added to make it compliant
    
    Format your response in a clear, structured manner.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a policy compliance expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    
    return response.choices[0].message['content']

def main():
    st.title("Policy Compliance Review Tool")
    st.write("Upload a policy document and specify the security standard and controls to check for compliance.")
    
    uploaded_file = st.file_uploader("Upload Policy Document", type=['pdf', 'docx'])
    standard_name = st.text_input("Enter Security Standard Name (e.g., ISO 27001, NIST 800-53)")
    controls_description = st.text_area("Enter Controls Description", 
                                      height=150,
                                      placeholder="Describe the specific controls you want to check for compliance...")
    
    if st.button("Analyze Compliance") and uploaded_file and standard_name and controls_description:
        with st.spinner("Analyzing document..."):
            try:
                # Extract text based on file type
                if uploaded_file.name.endswith('.pdf'):
                    document_text = extract_text_from_pdf(uploaded_file)
                elif uploaded_file.name.endswith('.docx'):
                    document_text = extract_text_from_docx(uploaded_file)
                else:
                    st.error("Unsupported file format")
                    return
                
                # Analyze compliance
                analysis_result = analyze_policy_compliance(document_text, standard_name, controls_description)
                
                # Display results
                st.subheader("Compliance Analysis Results")
                st.markdown(analysis_result)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
