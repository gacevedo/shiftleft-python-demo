from flask_webgoat import create_app

app = create_app()

@app.after_request
def add_csp_headers(response):
    # Broken Access Control - Fixed
    response.headers['Access-Control-Allow-Origin'] = 'https://trusted-domain.com'  # Replace with your trusted domain
    # Security Misconfiguration - Fixed
    response.headers['Content-Security-Policy'] = "script-src 'self'"
    return response


if __name__ == '__main__':
    app.run()

