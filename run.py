from app import create_app
#from error_handlers import page_not_found
import os

config_name = os.getenv('APP_SETTINGS', 'development')

app = create_app(config_name)


if __name__ == '__main__':
    app.run()