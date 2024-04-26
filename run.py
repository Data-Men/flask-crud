from app import app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# If this script is executed directly
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    
    hostname = os.getenv('HOSTNAME', '0.0.0.0')

    app.run(host=hostname, port=port,debug=True)