from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
  return "Hello Anees 234"

if __name__ == "__main__":
  print("I am inside __main__")
  app.run('0.0.0.0', debug=True)
  
