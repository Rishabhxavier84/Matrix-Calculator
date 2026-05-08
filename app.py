from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def home():
    return "Hello"

@app.route("/api/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("index.html")
    else:
        mat1 = request.form["mat1"].strip().split("\n")
        matrix1 = []
        for idx in mat1:
            matrix1.append(list(map(int, idx.split())))
        
        mat2 = request.form["mat2"].strip().split("\n")
        matrix2 = []
        for idx in mat2:
            matrix2.append(list(map(int, idx.split())))
        matrix1 = np.array(matrix1)
        matrix2 = np.array(matrix2)
        # result = np.matmul(matrix1, matrix2)
        result = matrix1 + matrix2
        return render_template("result.html", result = result.tolist())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)