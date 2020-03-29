__author__ = 'Jesse Bartola'

import os
from app import create_flask_app


if __name__ == "__main__":
    app = create_flask_app()
    app.run(debug=os.environ.get('ENVIRONMENT', 'prod') == 'dev', host='0.0.0.0', port=os.environ.get('PORT', 3000))
