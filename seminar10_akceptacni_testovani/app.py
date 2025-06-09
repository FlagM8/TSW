from flask import Flask, request, redirect, render_template, make_response

app = Flask(__name__)
data = []

@app.route('/')
def home():
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Robot FW hlavni strana</title>
</head>
<body>
    <h1>Robot FW hlavni strana</h1>
    <a href='/form'>Testovaci form</a>
</body>
</html>"""
    return make_response(html, 200, {"Content-Type": "text/html; charset=utf-8"})

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            data.append({'name': name, 'email': email})
            return redirect('/list')
    return render_template('form.html')

@app.route('/list')
def list_entries():
    return render_template('list.html', entries=data)

@app.route('/reset')
def reset():
    data.clear()
    return "Smazano!"

if __name__ == "__main__":
    app.run(debug=True)