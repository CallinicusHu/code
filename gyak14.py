from flask import Flask, session, redirect, url_for, request
from flask import render_template
import requests

panda = Flask(__name__)
panda.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@panda.route('/')
def index():
    return render_template('index.html')

@panda.route("/my-link", methods=['GET', 'POST'])
def question():
    if (request.method == 'GET'):
        country = request.args.get("country")
        api_url = f'https://api.api-ninjas.com/v1/vat?country={country}'
        response = requests.get(api_url, headers={'X-Api-Key': 'BV+aVla8SvDJx22cAlWr3w==l4k92B43b912ca50'})
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return "Error:", response.status_code, response.text

        if country == "HU":
            return render_template('hu_vat.html')
        if country == "DE":
            return render_template('de_vat.html')
        if country == "FR":
            return render_template('fr_vat.html')
        else:
            return "el lett baszva"
    return "ez is el lett baszva"


panda.run()
