from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h2>온도 변환기</h2>
        <form action="/temp">
            <input type="text" name="temp" placeholder="온도 입력">
            <select name="choice">
                <option value="℃">℃ → ℉</option>
                <option value="℉">℉ → ℃</option>
            </select>
            <button type="submit"style="background-color: #87CEEB;">변환</button>
        </form>
    </body>
    </html>
    """
def c2f(c):
    return c * 9/5 + 32

def f2c(f):
    return (f-32) * 5/9

@app.route("/temp")
def temp():
    temp = request.args.get("temp")
    choice = request.args.get("choice")

    if choice == "℃":
        result = c2f(float(temp))
        unit = "℉"
    else:
        result = f2c(float(temp))
        unit = "℃"

    return f"{temp} {choice} = {result:.2f} {unit}"

app.run(debug=True)