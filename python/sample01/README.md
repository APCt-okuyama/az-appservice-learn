# backend_pythons

## Python開発環境 セットアップ

Pythonのバージョン
```
python3 -V 
Python 3.8.10
```

仮想環境を作成する
```
python3 -m venv venv
```

仮想環境を有効にする　※コマンドに (venv)と表示されます。
```
. venv/bin/activate
(venv) apc-user@:backend_python$
```

ライブラリのインストール
```
pip install -r requirements.txt
```

実行(ローカル環境で動作確認)
```
export FLASK_APP=app.py
flask run (or python3 -m flask run)
flask run --host=0.0.0.0
```
※--host=0.0.0.0 外部からの接続を可能にする



# CLIコマンドでApp Serviceへデプロイする

App Service プランとApp Service
```
export ResourceGroup=az-appservice-example
# App Service プランを作成 (linux, sku B1で作成)
# sku B1: コア数 1, RAM 1.75GB 8212円/月 
az appservice plan create -g $ResourceGroup -l japaneast -n my-example-app-plan --sku B1 --is-linux

# App Serviceをデプロイ
# ※requirements.txtがあるのでPythonと判断される
az webapp up -n my-example-app-py -g $ResourceGroup -l japaneast -p my-example-app-plan --runtime 'PYTHON:3.8'
```

確認
```
curl https://my-example-app-py.azurewebsites.net/
<p>Hello, World! im woring2.</p>
```

# カスタムコンテナとしてApp Serviceへデプロイする

https://docs.microsoft.com/ja-jp/azure/app-service/tutorial-custom-container?pivots=container-linux

基本的な手順は
```
カスタム Docker イメージを Azure Container Registry にプッシュする
App Service にカスタム イメージをデプロイする
```
の２つ。

##  Docker コンテナ

build
```
docker build -t tokym/my-python-app:v1 .
docker run --rm -p 8080:5000 tokym/my-python-app:v1 
```

push (docker hub)
```
docker login
docker push tokym/my-python-app:v1
```

## App Serviceへのデプロイ

プランを作成 (--is-linux)
```
export ResourceGroup=az-appservice-example
az appservice plan create --name my-example-app-plan --resource-group $ResourceGroup --is-linux
```

WEBアプリを作成
```
az webapp create --resource-group $ResourceGroup --plan my-example-app-plan --name my-pythonapi-container-app --deployment-container-image-name tokym/my-python-app:v1
```

WEBSITES_PORTを設定(app serviceで公開されるport(443)にマッピングされる) デフォルトでは80がマッピングされている
```
az webapp config appsettings set --resource-group $ResourceGroup --name my-pythonapi-container-app --settings WEBSITES_PORT=5000
```

コンテナを更新 (v1からv2に変更)
```
az webapp config container set --name my-pythonapi-container-app --resource-group $ResourceGroup --docker-custom-image-name tokym/my-python-app:v2 --docker-registry-server-url https://tokym
```

app serviceの再起動
```
az webapp restart --name my-pythonapi-container-app --resource-group $ResourceGroup
```

確認
```
curl -i https://my-pythonapi-container-app.azurewebsites.net
```

コンテナーのログ記録を有効にする
```
az webapp log config --name my-pythonapi-container-app --resource-group $ResourceGroup --docker-container-logging filesystem
```

log tail
```
az webapp log tail --name my-pythonapi-container-app --resource-group $ResourceGroup
```

## App Serviceへのデプロイ(CICD設定)

```
az webapp deployment container config --enable-cd true --name my-example-container-app --resource-group $ResourceGroup --query CI_CD_URL --output tsv
```
CI_CD_URLはApp Serviceによって生成されるURL、これをDockerHubのWebhooksに登録することでイメージが更新されるタイミングでデプロイが実行される
