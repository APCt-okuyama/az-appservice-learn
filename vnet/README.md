# VNet統合

SQL Serverを利用するので自分でDBを準備する必要がある。
https://docs.microsoft.com/ja-jp/azure/app-service/tutorial-dotnetcore-sqldb-app?tabs=azure-portal%2Cazure-cli-deploy%2Cdeploy-instructions-azure-portal%2Cazure-portal-logs%2Cazure-portal-resources#3---create-the-database

https://training-vnet-integration.scm.azurewebsites.net:443/training-vnet-integration.git



```
az sql server create --location japaneast --resource-group $ResourceGroup --name trainingdb001 --admin-user myadminuser --admin-password Password@123
```

```
az sql db create --resource-group $ResourceGroup --server trainingdb001 --name coreDb
```

```
az sql server firewall-rule create --resource-group $ResourceGroup --server trainingdb001 --name AzureAccess --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0
```
    
```
az sql db show-connection-string --client ado.net --name coreDb --server trainingdb001
```

Server=tcp:trainingdb001.database.windows.net,1433;Database=coreDb;User ID=myadminuser;Password=Password@123;Encrypt=true;Connection Timeout=30

az webapp config connection-string set \
    -g msdocs-core-sql \
    -n <your-app-name> \
    -t SQLServer \
    --settings MyDbConnection=<your-connection-string>