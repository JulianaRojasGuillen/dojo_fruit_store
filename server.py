from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

listaRegistros=[]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout',methods=['GET'])
def despliegaCheckout():

    return render_template("checkout.html",nuevoRegistro=listaRegistros[0])

@app.route('/registroCompra', methods=['POST'])         
def checkout():
    nuevoRegistro={
        "numberStrawberry": request.form["strawberry"],
        "numberRaspberry": request.form["raspberry"],
        "numberApple": request.form["apple"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "student_id": request.form["student_id"]
        }
    listaRegistros.clear()
    listaRegistros.append(nuevoRegistro)
    print(request.form)
    return redirect ('/checkout')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)