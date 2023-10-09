from sports_app.settings import *

TEST = True


REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/minute",
    },
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}
