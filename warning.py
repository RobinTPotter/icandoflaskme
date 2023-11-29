import subprocess

def app(enciron, start_response):
    subprocess.call(["play","large_drink.wav"])
    status = "200 OK"
    response_headers = [
        ("Content-type", "text/plain"),
        ("Content-Length", "2")
    ]
    start_response(status, response_headers)
    return iter([b"hi"])

