from datetime import timedelta
# import os

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]
}

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
]


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,

    # "SIGNING_KEY": os.environ.get('SECRET_KEY_JWT'),
    "SIGNING_KEY": 'ug34vti4-tui4t_t,p34cr3,4_çcr;4k3t349)çkcto3c,34eop,',

    "AUTH_HEADER_TYPES": ("Bearer",),
}
