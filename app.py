from website import create_app

app, _ = create_app()
client = app.test_client()

if __name__ == '__main__':
    app.run()
