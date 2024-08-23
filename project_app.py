import webbrowser
import pandas as pd
print('project_app.py is running')
df = pd.read_json('data.json')
html_file_spec = "data.html"
df.to_html(html_file_spec)
webbrowser.open(html_file_spec)