from flask_webgoat import create_app

app = create_app()

@app.after_request
def add_csp_headers(response):
    # Only allow requests from trusted domains
    response.headers['Access-Control-Allow-Origin'] = 'https://trusted-domain.com'
    # Set Content-Security-Policy to a strict value
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'"
    return response



if __name__ == '__main__':
    app.run()


