from flask import Flask, request, render_template
import Frutas
app = Flask(__name__,template_folder='html')

@app.route("/", methods=['GET'])
def frutas():
    return render_template("start_frutas.html")

@app.route("/mostrar_frutas", methods=['POST'])
def mostrar_frutas():
 # Obtener la fruta seleccionada por el usuario
    fruta_ingresada=request.form["fruta"]
    cantidad_ingresada= int(request.form["cantidad"])
    
 # Insertar el código aquí
    if fruta_ingresada=='Manzana':
       variedad_ingresada=request.form["variedad"]
       fruta =Frutas.Manzana(fruta_ingresada, cantidad_ingresada, variedad_ingresada)
    elif fruta_ingresada=='Banana':
        madurez_ingresado= request.form["madurez"]
        fruta =Frutas.Banana(fruta_ingresada, cantidad_ingresada, madurez_ingresado)
    elif fruta_ingresada=='Naranja':
        dulzor_ingresado= request.form["dulzor"]
        fruta =Frutas.Naranja(fruta_ingresada, cantidad_ingresada, dulzor_ingresado)
       
 # Renderizar la página de frutas con la fruta seleccionada
    return render_template("frutas.html", fruta=fruta)



if __name__ == '__main__':
   app.run(debug=True)