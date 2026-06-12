from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    data = request.args.get('data', '2013-03-12')
    url = f'https://api.nasa.gov/planetary/apod?api_key=1ZoAIosng9t1bPCyG8uXWDejAjrpYEiJ330G3L4t&date={data}'
    resultado = requests.get(url)
    dados_nasa = resultado.json()
    
    return render_template('index.html', info=dados_nasa, dados_atual=data)
    
if __name__ == '__main__':
    app.run(debug=True)