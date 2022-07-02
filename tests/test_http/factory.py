from typing import Dict, Any


def simple_get_request(path: str, *, extra_headers: Dict[str, Any] = None):
    extra_headers = extra_headers or {}

    event = {
        "version": "2.0", "routeKey": "$default", "rawPath": path, "rawQueryString": "",
        "headers": {
            "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256", "x-amzn-tls-version": "TLSv1.2",
            "x-amzn-trace-id": "Root=1-62bb252d-1d7f3e030c92ebf435c41bc1", "x-forwarded-proto": "https",
            "host": "gxn4ocnpcc2fg65qqfmkdrl4li0ohyvw.lambda-url.ap-southeast-1.on.aws", "x-forwarded-port": "443",
            "x-forwarded-for": "127.0.0.1", "accept-encoding": "gzip, deflate", "accept": "*/*",
            "user-agent": "python-requests/2.27.1",
            **extra_headers,
        }, "requestContext": {
            "accountId": "anonymous", "apiId": "gxn4ocnpcc2fg65qqfmkdrl4li0ohyvw",
            "domainName": "gxn4ocnpcc2fg65qqfmkdrl4li0ohyvw.lambda-url.ap-southeast-1.on.aws",
            "domainPrefix": "gxn4ocnpcc2fg65qqfmkdrl4li0ohyvw",
            "http": {
                "method": "GET", "path": path, "protocol": "HTTP/1.1",
                "sourceIp": "49.49.237.96",
                "userAgent": "python-requests/2.27.1",
            }, "requestId": "b0d049da-f0d3-4bac-9f90-f1a623b43075", "routeKey": "$default",
            "stage": "$default", "time": "28/Jun/2022:15:58:37 +0000", "timeEpoch": 1656431917279,
        }, "isBase64Encoded": False}
    return event
