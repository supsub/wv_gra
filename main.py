import time

PASSWORD_LINK_MAPPING = {
    
# 
# fill this !!!
#

}

def main(request):
    # For more information about CORS and CORS preflight requests, see:
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    time.sleep(2)

    if request.args and 'guess' in request.args:
        result = PASSWORD_LINK_MAPPING.get(request.args.get('guess')) or "Wrong password"
    else:
        result = "You have to provide `guess` query param to your http request"

    return (result, 200, headers)
