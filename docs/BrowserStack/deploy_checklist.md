# Step 1: Pull supragya
```bash
cd ~/supragya
git checkout master
git pull
```

# Step 2: Create Screen and cd

## Deploy1
```bash
screen -S supragya-deploy
cd ~/deploy
```

# Step 3: Run Stubs

## Mac STUB
```bash
get checkout master
git pull
git checkout -b "Supragya"
pd ~/supragya/docs/BrowserStack/dplmac.json
```
## Win STUB
```bash
get checkout master
git pull
git checkout -b "Supragya"
pd ~/supragya/docs/BrowserStack/dplwin.json
```

# Step 3: Check states

[Check Deployment deploy1 DB](http://deploy.bsstag.com/deploy_status/1)

[Check Deployment deploy2 DB](http://deploy.bsstag.com/deploy_status/2)

[Check Deployment deploy3 DB](http://deploy.bsstag.com/deploy_status/3)

[Deploy Query](https://deploy.bsstag.com/deploy_query)

```sql
SELECT * from terminals_mac order by deployed
```

