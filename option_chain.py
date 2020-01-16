from tdameritrade import TDClient
import numpy as np

from mappers import map_option_chain

from datetime import datetime, timedelta

# This token has expired by now, so don't bother using it :)
TOKEN = '6xM5/g4qhw1v5Ll7v6ml4vbMRF7Y7afPYPB/EJ8rNXmlhzFd+amUE4olSQICqXTSjpvEE7EnpU4joCTQyUWDCLBS8cHDZBt4RBGMSi6veKJftFrYxLPw29bPWvFqkIU0gtbutdr3Gz8uVACu2UmpeLXxvIaFh+w0YlbumHwndiw5Mmh7Lj6nGLLPsOoBdt+Q9VPyWw0eIxcWhCBXA/AueygVrf681OfwzydP1JPoey3Vcx7LqADx+Y7eCi707/G6aSzANF9DxFx1+xjg9YRnYFYOVprhPdqrHpN9Nj1WiWJ/nRosNrLCz+zpq/BDkUP+FeHEjer2bRgU6tmLi0T0qc39Gc56Otwt6kz4RTv55OCLIRe26gR8sRZ2PG8xkAQH/dQpoW0AI2XjQaR8Ni2w9BBHH9EVbrXT2GCNuJFAjcui1HHy6/4YKXMXNupnwXBRhAWxjKeNFjkHpEemaezjjHDlOST4AFx5NaFdypnnslwrdh+ap7ymZpScnHRqHnUyDUEA66uBs3GKbCeAAFxiDAOf47EAS5QnG1A4w3+9eWXuL1TLT100MQuG4LYrgoVi/JHHvlp1pJhg1BhRLlcqwJNk8wCrohB5qUIDsg7O+NvDVQNkErEBvr8mZ0N7c0tsZVjxIcvc2zTilB/qstp0DIQPC83MzZXgxRS8AlG5bXHTbqPRTNcFIce3Ak1Ax3aXLfGQsldOQ5hv+NbOIqgrvOBzPgHxVvhx0vLDiWcAE0wm2YYxB0g9s3op5Je3aAtc9SXCmhpKI0bd8khrLaVncarjwXrfAR1phSmrUHmWG76jv9YilzaoZugZ9zeVZpc++j5Wg8EisJjANiAsfTJ+DivC8e5pKYZ7KidT/Y9MT03ZWhuWhfZDg/R1gIvU781++ecZ0Ln8C/KGSRRlHn0E539+c9Aem9RX/KZSIRnpv0zEa3AwA1E2d0wlkcCa7QkdKKq+mAsC8To0H339lJpuNg2KNmlmjX9DGvS+MkqgwgGDlts8m2AO9pm11JIcGXzL/yGqsJ0wbnpY1WwJk7zcom4uv4xFhFKQ08qAM5Zci6cx5Mb2hRXjy74voNjQvuxfYjKZWwqoZufDcO8rkLCQgMNilwah70RMgAC5F2JxF/NygJIOKN+4Aw==212FD3x19z9sWBHDJACbC00B75E'

c = TDClient(TOKEN)

def get_option_chain(symbol, low_dte=30, high_dte=45, min_volume=50):
    from_date = (datetime.now() + timedelta(days=low_dte)).isoformat()
    to_date = (datetime.now() + timedelta(days=high_dte)).isoformat()

    data = c.options(symbol, strategy='ANALYTICAL', fromDate=from_date, toDate=to_date, optionType='S')
    call_data = data['callExpDateMap']
    put_data = data['putExpDateMap']

    volume_filter = lambda option: option['totalVolume'] < min_volume

    return {'CALL': map_option_chain(call_data, volume_filter), 'PUT': map_option_chain(put_data, volume_filter)}

def get_price_quote(symbol):
    return c.quote(symbol)[symbol.upper()]['lastPrice']