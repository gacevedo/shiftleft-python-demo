from flask_webgoat import create_app

app = create_app()

@app.after_request
def add_csp_headers(response):
    # Removed wildcard from CORS header
    response.headers['Access-Control-Allow-Origin'] = 'trusted-domain.com'
    # Removed 'unsafe-inline' from CSP header
    response.headers['Content-Security-Policy'] = "script-src 'self'"
    return response


if __name__ == '__main__':
    app.run()

