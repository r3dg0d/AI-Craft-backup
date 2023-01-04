print("A    I    C    R    A    F    T")

from pyngrok import ngrok

def run_ngrok():
  # Start ngrok
  public_url = ngrok.connect(port="8080", proto="http")
  print(f"Running on {public_url}")

run_ngrok()
