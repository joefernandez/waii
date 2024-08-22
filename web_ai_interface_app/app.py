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
import markdown

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    """Set up web interface and handle POST input."""
    process_message = create_message_processor()

    if request.method == 'POST':
        prompt = get_prompt()
        customer_request = request.form['request']
        prompt += customer_request
        result = process_message(prompt)
        result = markdown.markdown(result)
        # re-render page with data:
        return render_template('index.html', request=customer_request, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

def get_prompt():
    return "Extract the relevant details of this request and return them as a list:\n"

def create_list(text):
    """
    Processes the JSON returned by the model and puts it into an HTML-friendly format.

    Args:
         text: The string to process.

    Returns:
         The processed HTML, or the original string if the JSON is not formatted with
         Markdown.
    """

    text = text.splitlines()
    text = text[2:-1]
    for x,s  in enumerate(text):
         if text[x].endswith(","):
              s = s[:-1]

         s = s.replace('"', '')
         s = s.replace('_', ' ')
         text[x] = "<li>" + s + "</li>"
    text = "\n".join(text)
    return text

def scrub_markdown(text):
    if text.startswith("```json"):
         text = text.replace("```json", "")
         text = text.replace("```", "")
    return text
