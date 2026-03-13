from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/push', methods=['POST'])
def push():
    try:
        # شغلي السكريبت بتاعك
        result = subprocess.run(['python', 'E:/mariam/first-app/auto_push.py'], 
                                capture_output=True, text=True)
        return jsonify({"message": "تم بنجاح", "output": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)