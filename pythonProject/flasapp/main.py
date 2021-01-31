from flask import Flask, render_template
app = Flask(__name__)
#decorator
@app.route("/hello")
def main():
   return render_template('index.html')
   # return "hello guys how are you"

if __name__ == "__main__":
   app.run()