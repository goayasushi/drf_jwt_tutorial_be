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

### その他

#### ecs エラー

- ec2 を private サブネットに配置した場合に、ec2 インスタンスの登録がされない

  インターネット接続が必要と思われる

  https://dev.classmethod.jp/articles/privatesubnet_ecs/

  `/var/log/ecs/ecs-agent.log`

  ```
  evel=info time=2025-02-11T01:21:31Z msg="Loading state!" module=state_manager.go
  level=info time=2025-02-11T01:21:31Z msg="Event stream ContainerChange start listening..." module=eventstream.go
  level=info time=2025-02-11T01:21:31Z msg="eni watcher has been initialized" module=watcher_linux.go
  level=info time=2025-02-11T01:21:31Z msg="Successfully got ECS instance credentials from provider: EC2RoleProvider"
  level=info time=2025-02-11T01:21:31Z msg="Successfully loaded Appnet agent container tarball: /managed-agents/serviceconnect/ecs-service-connect-agent.interface-v1.tar" image="ecs-service-connect-agent:interface-v1"
  level=info time=2025-02-11T01:21:31Z msg="Registering Instance with ECS"
  level=info time=2025-02-11T01:21:31Z msg="Remaining memory" remainingMemory=952
  level=error time=2025-02-11T01:22:01Z msg="health check [HEAD http://localhost:51678/v1/metadata] failed with error: Head \"http://localhost:51678/v1/metadata\": dial tcp 127.0.0.1:51678: connect: connection refused" module=healthcheck.go
  level=error time=2025-02-11T01:22:31Z msg="health check [HEAD http://localhost:51678/v1/metadata] failed with error: Head \"http://localhost:51678/v1/metadata\": dial tcp 127.0.0.1:51678: connect: connection refused" module=healthcheck.go
  level=error time=2025-02-11T01:23:01Z msg="health check [HEAD http://localhost:51678/v1/metadata] failed with error: Head \"http://localhost:51678/v1/metadata\": dial tcp 127.0.0.1:51678: connect: connection refused" module=healthcheck.go
  level=error time=2025-02-11T01:23:31Z msg="health check [HEAD http://localhost:51678/v1/metadata] failed with error: Head \"http://localhost:51678/v1/metadata\": dial tcp 127.0.0.1:51678: connect: connection refused" module=healthcheck.go
  level=error time=2025-02-11T01:23:32Z msg="Unable to register as a container instance with ECS" error="RequestError: send request failed\ncaused by: Post \"https://ecs.ap-northeast-1.amazonaws.com/\": dial tcp 52.195.202.50:443: i/o timeout"
  level=error time=2025-02-11T01:23:32Z msg="Error registering container instance" error="RequestError: send request failed\ncaused by: Post \"https://ecs.ap-northeast-1.amazonaws.com/\": dial tcp 52.195.202.50:443: i/o timeout"
  ```

  ->natgateway / vpc エンドポイントの設置でインターネット接続設定したいところだが、料金がかかるので ec2 を public サブネットに配置することにする

  _セキュリティを考慮して sg の設定は最小限にする_

- awsvpc モードでコンテナに接続できない

  https://zenn.dev/neko_student/articles/258cbed688e469
  https://qiita.com/k2-hara/items/bb2ebb3bc5efc3000729#4-2-%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E5%95%8F%E9%A1%8C

  ->今回は、bridge モードで対応する。

- 400bad request になる

  ALLOWED_HOSTS に追加が必要
  https://office54.net/python/django/settings-allowed-hosts

  ```
  ALLOWED_HOSTS = ["リクエスト時のホスト"]
  ```
