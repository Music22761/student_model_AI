from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LogisticRegression
import pickle

load_model = pickle.load(open('student_model.pkl', 'rb'))

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return jsonify("Hello World")

@app.route('/predict', methods=['POST'])
def predict():
    
    result = ""
    try:
        # รับข้อมูล time_study จากคำขอ POST
        data = request.get_json()['time']

        # คำนวณผลลัพธ์
        prediction = load_model.predict([[data]])

        # คืนค่าผลลัพธ์เป็น JSON
        
        
        if not isinstance(data, str):
            
            response = {
                'ประเมินว่า ': prediction[0]
            } 
            
        else:
            result = 'ข้อมูลที่ป้อนเข้ามาไม่ใช่ตัวเลข กรุณาป้อนใหม่'   
        
         

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
