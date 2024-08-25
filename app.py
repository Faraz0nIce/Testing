from flask import Flask, render_template, request

app = Flask(__name__)

slip_count = 1

@app.route("/")
def index():
    return render_template("index.html", slip_count=slip_count)

@app.route("/next", methods=["GET"])
def next_slip():
    global slip_count
    slip_count += 1
    new_slip_html = """
        <div class="slip">
            <div class="slip-img">
                <img src="https://via.placeholder.com/60" alt="Slip Image">
            </div>
            <div class="slip-info">
                <h3>Slip {}</h3>
                <p>Description of the slip</p>
            </div>
        </div>
    """.format(slip_count)
    return new_slip_html

if __name__ == "__main__":
    app.run(debug=True)