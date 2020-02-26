# Step 1: Pull supragya
```
cd ~/supragya
git checkout master
git pull
```

# Step 2: Run Stub

## Mac STUB
```
get checkout master
git pull
git checkout -b "Supragya"
pd ~/supragya/docs/dplmac.json
```
## Win STUB
```
get checkout master
git pull
git checkout -b "Supragya"
pd ~/supragya/docs/dplwin.json
```

# Step 3: Check states

## Check state
[Check Deployment deploy1 DB]("http://deploy.bsstag.com/deploy_status/1")

[Check Deployment deploy2 DB]("http://deploy.bsstag.com/deploy_status/2")

[Check Deployment deploy3 DB]("http://deploy.bsstag.com/deploy_status/3")

[Deploy Query]("https://deploy.bsstag.com/deploy_query")

`SELECT * from terminals_mac order by deployed`