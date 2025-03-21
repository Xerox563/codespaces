from flask import Flask
import subprocess
import os
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
  
    full_name = "Amit Gangwar"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    
   
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

   
    top_output = subprocess.getoutput("top -b -n 1")

   
    response = f"""
    <h2>Name: {full_name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
