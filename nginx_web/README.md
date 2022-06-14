# nginxをカスタムコンテナとしてデプロイする

SPAをホスティングしたnginxをデプロイしてみる


## Docker / Nginx Image

docker version
```
Version:          20.10.14
```

新しいバージョンで軽量のalpineを選択
```
docker pull nginx:1.22.0-alpine
```

# docker imageを作成してApp Serviceにコンテナとしてデプロイ

```
docker build -t tokym/nginx_test:v1 .
docker run --rm --name my_nginx_test -d -p 8080:80 tokym/nginx_test:v1
```

```
curl http://localhost:8080
test this is index.html
```

Docker Hub へ Push
```
docker login
docker push tokym/nginx_test:v1
docker search tokym
```

## App Service作成

プランを作成 (--is-linux)
```
az appservice plan create --name my-example-app-plan --resource-group $ResourceGroup --is-linux
```

WEBアプリを作成
```
az webapp create --resource-group $ResourceGroup --plan my-example-app-plan --name my-example-container-app --deployment-container-image-name tokym/nginx_test:v1
```

WEBSITES_PORTを設定(app serviceで公開されるport(443)にマッピングされる)
```
az webapp config appsettings set --resource-group $ResourceGroup --name my-example-container-app --settings WEBSITES_PORT=80
```

curlで確認
```
curl https://my-example-container-app.azurewebsites.net/
test this is index.html
```