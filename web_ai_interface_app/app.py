#
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import Flask, render_template, request
from web_ai_interface_app.models.gemini import create_message_processor

app = Flask(__name__, static_url_path='/static', static_folder='static')
customer_request = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global customer_request
    """Set up web interface and handle POST input."""
    process_message = create_message_processor()

    # First run behavior: load a test email
    if customer_request is None:
        customer_request = get_test_email()
        return render_template('index.html', request=customer_request)

    # Process email data
    if request.method == 'POST':
        prompt = get_prompt()
        customer_request = request.form['request']
        prompt += customer_request
        result = process_message(prompt)
        result = strip_markdown(result)
        # re-render page with data:
        return render_template('index.html', request=customer_request, result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

def get_prompt():
    return "Extract the relevant details of this request and return them in JSON format:\n"

def strip_markdown(text):
  if text.startswith('```json') and text.endswith('```'):
     text = text.replace('```json', '')
     text = text.replace('```', '')
     text = text.strip()

  return text

def get_test_email():
    try:
        with open('data/email-001.txt', 'r') as file:
            email_content = file.read()
    except FileNotFoundError:
        email_content = "Error: File not found!"
    return email_content