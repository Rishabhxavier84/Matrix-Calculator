from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def home():
    return "Hello"

@app.route("/api/calculator", methods=["GET", "POST"])
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
        operations = request.form["operations"]
        try:
            matrix1.shape == matrix2.shape
            if operations == "add":
                result = matrix1 + matrix2
            elif operations == "sub":
                result = matrix1 - matrix2
            elif operations == "norm_mul":
                result = matrix1 * matrix2
            elif operations == "mat_mul":
                result = np.matmul(matrix1, matrix2)
            elif operations == "transpose":
                result = matrix1.T
            return render_template("result.html", result = result.tolist())
        except Exception as e:
            return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)