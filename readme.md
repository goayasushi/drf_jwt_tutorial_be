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

### django

#### マイグレーション

- マイグレーションファイルの作成

  - プロジェクト内のすべてのアプリケーションのモデル変更を検出して、マイグレーションファイルを生成

  ```
  python manage.py makemigrations
  ```

  - 特定のアプリケーションのモデル変更を検出して、マイグレーションファイルを生成

  ```
  python manage.py makemigrations 【app_name】
  ```

- マイグレーションの適用

  - プロジェクト内のすべてのアプリケーションのマイグレーションを適用

  ```
  python manage.py migrate
  ```

  - 特定のアプリケーションのマイグレーションを適用

  ```
  python manage.py migrate 【app_name】
  ```

### docker

#### psql 接続

コンテナの Exec で以下のコマンドを実行
https://zenn.dev/azuki9140/articles/7a9426295814ce

```
psql -h db -U myappuser -d drf_jwt_turorial
psql -h 【ホスト名】 -U 【ユーザー名】 -d 【db名】
```

### ローカル起動

- 環境変数の設定

  .env ファイルを作成し、任意の設定値を記述

  ```
  DATABASE_NAME=データベース名
  DATABASE_USER=ユーザー名
  DATABASE_PASSWORD=ユーザーで接続する際のパスワード
  DATABASE_HOST=ホスト名
  DATABASE_PORT=ポート番号
  ```

- 起動

```
docker compose up --build -d
```

- リクエスト

  任意のクライアントツールからリクエストを実行

  - postman でユーザー登録リクエスト例
    - メソッド: `POST`
    - URL: `http://localhost:8000/account/register/`
    - リクエストボディ
      ```
      {
          "username": "test-user",
          "password": "test",
          "first_name": "テスト",
          "last_name": "登録",
          "email": "register@test.com"
      }
      ```
