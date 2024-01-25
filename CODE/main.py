from apps.views import app

def main():
    app.run(debug=True, host='::', port=5000)

if __name__ == '__main__':
    main()