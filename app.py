from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def home():
    return "Matrix Calculator"




#creates the matrix and handles the error
def matrix_creator(num):
    mat = request.form[f"mat{num}"].strip().split("\n")
    matrix = []
    for idx in mat:
        try:
            matrix.append(list(map(int, idx.strip().split())))
        except ValueError:
            raise ValueError(f"The Matrix {num} must have only numbers.\n No characters or numbers allowed.")
    return np.array(matrix)





@app.route("/api/calculator/two-matrix", methods=["GET", "POST"])
def operations():
    if request.method == "GET":
        return render_template("index.html")
    else:
        try:
            # mat1 = request.form["mat1"].strip().split("\n")
            # matrix1 = []
            # for idx in mat1:
            #     try:
            #         matrix1.append(list(map(int, idx.strip().split())))
            #     except ValueError:
            #         raise ValueError("Matrix 1 must have only numbers")

            # mat2 = request.form["mat2"].strip().split("\n")
            # matrix2 = []
            # for idx in mat2:
            #     try:
            #         matrix2.append(list(map(int, idx.strip().split())))
            #     except ValueError:
            #         raise ValueError("Matrix 2 must have only numbers")

            # matrix1 = np.array(matrix1)
            # matrix2 = np.array(matrix2)

            matrix1 = matrix_creator(1)
            matrix2 = matrix_creator(2)
            
            operations = request.form["operations"]

            if operations in ["add", "sub", "norm_mul", "div"]:

                if matrix1.size == 0 or matrix2.size == 0:
                    raise ValueError("Both matrices must contain the elements")

                if matrix1.shape != matrix2.shape:
                    raise ValueError("Matrices must have same shape.")

                if operations == "add":
                    result = matrix1 + matrix2

                elif operations == "sub":
                    result = matrix1 - matrix2

                elif operations == "norm_mul":
                    result = matrix1 * matrix2

                elif operations == "div":
                    if np.any(matrix2 == 0):
                        raise ValueError("The elements of the second matrix cannot be zero.")
                    result = np.round((matrix1 / matrix2), 2)

            elif operations == "mat_mul":
                if matrix1.size == 0 or matrix2.size == 0:
                    raise ValueError("Both matrices must contain the elements")

                if matrix1.shape[1] != matrix2.shape[0]:
                    raise ValueError("Columns of matrix 1 must be the same number as rows of matrix 2.")

                result = np.matmul(matrix1, matrix2)

            elif operations == "transpose":
                result = matrix1.T

            elif operations == "shape":
                result = np.array(matrix1.shape)

            elif operations == "flip":
                result = np.flip(matrix1)

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