from application_config import create_app

app = create_app()

def main():

  app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
  # we should instatiate the model here
  
  main()