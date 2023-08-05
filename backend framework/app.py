from flask import Flask, render_template, request
from new_file import main
app = Flask(__name__, template_folder=r"C:\Users\masge\Downloads\templates")

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("homepage.html")

@app.route('/2proj.html', methods=['GET', 'POST'])
def proj():
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
@app.route("/alpha.html",methods=['GET', 'POST'])
def alpha():
    user_input = ''  
    if request.method == 'POST':
        user_input = request.form['user_input']
        category =  'all categories'
        data_dict = main(category,user_input)  
        return render_template("results.html", data=data_dict)
    return render_template("alpha.html")
@app.route("/m1.html",methods=['GET', 'POST'])
def m1():
    pro='iphone 14 pro max'
    category =  'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)
@app.route("/m2.html",methods=['GET', 'POST'])
def m2():
    pro='oneplus 11 r'
    category = 'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)
@app.route("/m3.html",methods=['GET', 'POST'])
def m3():
    pro='samsung s23 ultra'
    category =  'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)
@app.route("/m4.html",methods=['GET', 'POST'])
def m4():
    pro='pixel 7 pro'
    category =  'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)
@app.route("/m5.html",methods=['GET', 'POST'])
def m5():
    pro='xiaomi 13 ultra'
    category =  'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)
@app.route("/m6.html",methods=['GET', 'POST'])
def m6():
    pro='huawei p9'
    category =  'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)
@app.route("/m7.html",methods=['GET', 'POST'])
def m7():
    pro='asus rog phone '
    category =  'mobiles'
    data_dict = main(category,pro)  
    return render_template("results.html", data=data_dict)

if __name__ == "__main__":
    app.run(debug=True)
