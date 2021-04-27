from flask import Flask
import requests
import pandas as pd

app = Flask(__name__)

URL = 'https://reqres.in/api/products/'

#Get contents of all pages from URL
url_contents = requests.get(URL).json()
product_info = url_contents["data"]
for page in range ( 2, url_contents["total_pages"]+1):
    url_contents = requests.get(URL + f"?page={page}").json()
    product_info.extend(url_contents["data"])

#Process and convert to  html format
df = pd.DataFrame(product_info)
df_html = df.to_html(index=False)


@app.route("/",methods=['GET'])
def home():
    return df_html

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')