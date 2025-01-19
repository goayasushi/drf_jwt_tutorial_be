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
    https://pypi.org/project/django-cors-headers/

### db

- postgresql
  https://pgsql-jp.github.io/current/html/
  https://docs.djangoproject.com/ja/5.1/ref/databases/#postgresql-notes

- ライブラリ
  psycopg2-binary
  https://www.psycopg.org/docs/install.html#quick-install
  https://zenn.dev/aew2sbee/articles/django-rest-framework-postgres

### env

- ライブラリ
  python-dotenv
  https://pypi.org/project/python-dotenv/
