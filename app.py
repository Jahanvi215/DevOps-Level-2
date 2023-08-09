from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitted_json = request.form.get('json_input')
        return jsonify(submitted_json)

    return render_template('level3_index.html')

print(render_template)

if __name__ == '__main__':
    app.run(debug=True, port=8000)