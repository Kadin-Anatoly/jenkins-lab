from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    student_name = os.getenv('STUDENT_NAME', 'Anatoly Kadin')
    return f'Hello, {student_name}!'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8072))
    app.run(host='0.0.0.0', port=port)
