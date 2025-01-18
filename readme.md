### jwt

- 今回の実装
  有効期限を 30m に設定。
  jwt token が期限内であれば、リクエストの度に jwt token の新規発行。

- ライブラリ
  https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

  - カスタマイズ
    https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

### cors

- ライブラリ
  https://pypi.org/project/django-cors-headers/

  - カスタムヘッダーの cors 設定
    CORS_EXPOSE_HEADERS
