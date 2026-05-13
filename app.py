from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def home():
    return "Matrix Calculator"

@app.route("/api/calculator", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("index.html")
    else:
        try:
            mat1 = request.form["mat1"].strip().split("\n")
            matrix1 = []
            for idx in mat1:
                matrix1.append(list(map(int, idx.strip().split())))

            mat2 = request.form["mat2"].strip().split("\n")
            matrix2 = []
            for idx in mat2:
                matrix2.append(list(map(int, idx.split())))

            matrix1 = np.array(matrix1)
            matrix2 = np.array(matrix2)
            
            operations = request.form["operations"]

            if operations in ["add", "sub", "norm_mul"]:

                if matrix1.shape != matrix2.shape:
                    raise ValueError("Matrices must have same shape")

                if operations == "add":
                    result = matrix1 + matrix2

                elif operations == "sub":
                    result = matrix1 - matrix2

                elif operations == "norm_mul":
                    result = matrix1 * matrix2

            elif operations == "mat_mul":
                if matrix1.shape[0] != matrix2.shape[1]:
                    raise ValueError("Columns of matrix 1 must be the same number as rows of matrix 2")

                result = np.matmul(matrix1, matrix2)

            elif operations == "transpose":
                result = matrix1.T

            # else:
            #     raise ValueError("Invalid operation.")

            return render_template("result.html", result = result.tolist())

        except ValueError as e:
            return render_template("errors/error.html", result = f"Input Error: {str(e)}")

        except Exception as e:
            return render_template("errors/error.html", result = f"Error: {str(e)}")
        


#error pages
@app.errorhandler(404)
def error_404(e):
    return render_template("errors/404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)












# try:
#                 if matrix1.shape != matrix2.shape:
#                     raise ValueError("Matrices must have same dimensions")
#                 if operations == "add":
#                     result = matrix1 + matrix2
#                 elif operations == "sub":
#                     result = matrix1 - matrix2
#                 elif operations == "norm_mul":
#                     result = matrix1 * matrix2
#                 elif operations == "mat_mul":
#                     result = np.matmul(matrix1, matrix2)
#                 elif operations == "transpose":
#                     result = matrix1.T
#                 return render_template("result.html", result = result.tolist())
#             except Exception as e:
#                 return f"Error: {str(e)}"