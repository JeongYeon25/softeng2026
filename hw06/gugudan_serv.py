from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("gugudan.html")


@app.route("/gugudan")
def gugudan():
    dan = request.args.get("dan")
    if not dan or not dan.isdigit():
        return "숫자를 입력해주세요!"

    dan = int(dan)

    gugu = ""
    for x in range(1, 10):
        gugu += f"<span style='color:gold'>{dan} x {x} = </span>"
        gugu += f"<span style='color:lightgreen'>{dan * x}</span><br>"

    return gugu


if __name__ == "__main__":
    app.run(debug=True)