from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')
    # return "Yes we are live"


@app.route('/prediction', methods=['POST'])
def predict_page():
    model = pickle.load(open('RandomForestRegressor2.pickle', "rb"))

    if request.method == 'POST':
        user_input1 = float(request.form.get('input1'))
        user_input2 = float(request.form.get('input2'))
        user_input3 = float(request.form.get('input3'))
        user_input4 = float(request.form.get('input4'))
        user_input5 = float(request.form.get('input5'))
        user_input6 = float(request.form.get('input6'))
        user_input7 = float(request.form.get('input7'))
        user_input8 = float(request.form.get('input8'))
        user_input9 = float(request.form.get('input9'))
        user_input10 = float(request.form.get('input10'))
        user_input11 = float(request.form.get('input11'))
        user_input12 = float(request.form.get('input12'))
        user_input13 = float(request.form.get('input12'))
        prediction = model.predict(
            ([[user_input1, user_input2, user_input3, user_input4, user_input5, user_input6,
               user_input7, user_input8, user_input9, user_input10, user_input11,
               user_input12,user_input13]]))

        return render_template("results.html", prediction=prediction.flatten()[0])


if __name__ == '__main__':
    app.run(debug=True)
