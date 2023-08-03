from flask import Flask, render_template, request
from new_file import main
app = Flask(__name__, template_folder=r"C:\Users\masge\Downloads\templates")
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("2proj.html")

@app.route("/books.html",methods=['GET', 'POST'])
def books():
    user_input = ''  
    if request.method == 'POST':
        user_input = request.form['user_input']
        category =  'books'
        data_dict = main(category,user_input)  
        return render_template("results.html", data=data_dict)
    return render_template("books.html")

@app.route("/ear.html",methods=['GET', 'POST'])
def ear():
    user_input = ''  
    if request.method == 'POST':
        user_input = request.form['user_input']
        category =  'earphones'
        data_dict = main(category,user_input)  
        return render_template("results.html", data=data_dict)
    return render_template("ear.html")

@app.route("/mobiles.html",methods=['GET', 'POST'])
def mobiles():
    user_input = ''  
    if request.method == 'POST':
        user_input = request.form['user_input']
        category =  'mobiles'
        data_dict = main(category,user_input)  
        return render_template("results.html", data=data_dict)
    return render_template("mobiles.html")

@app.route("/upcoming.html",methods=['GET', 'POST'])
def upcoming():
    return render_template("upcoming.html")

@app.route("/shoes.html",methods=['GET', 'POST'])
def shoes():
    user_input = ''  
    if request.method == 'POST':
        user_input = request.form['user_input']
        category =  'shoes'
        data_dict = main(category,user_input)  
        return render_template("results.html", data=data_dict)
    return render_template("shoes.html")
if __name__ == "__main__":
    app.run(debug=True)