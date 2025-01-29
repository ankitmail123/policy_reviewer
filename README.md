# Policy Compliance Review Tool

This tool uses AI to analyze policy documents and check their compliance against specified security standards and controls.

## Features

- Upload PDF or DOCX policy documents
- Specify security standards and controls for compliance checking
- Get detailed compliance analysis with:
  - Compliance status for each control
  - Supporting text from the document
  - Gap analysis and recommendations for non-compliant controls

## Local Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

1. Fork this repository to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and select your forked repository
4. In the Streamlit Cloud settings:
   - Add your OpenAI API key as a secret with the name: `OPENAI_API_KEY`
   - Set the Python version to 3.13
   - Set the main file path to: `app.py`

## Usage

1. Upload your policy document (PDF or DOCX format)
2. Enter the name of the security standard (e.g., ISO 27001, NIST 800-53)
3. Describe the specific controls you want to check for compliance
4. Click "Analyze Compliance" to get the results

## Note

Make sure you have a valid OpenAI API key with access to the GPT-4o-mini model for the best results.
