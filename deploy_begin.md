# Git PUll
```
git checkout master
git pull
```

# MAC

## JSON copy:
`vim dplmac.json`

`:set paste`
```
{
  "json_version" : 10, 
  "deployer" : "Supragya",
  "os" : "mac",
  "deploy_on_esxi" : false, 
  "run_only_once_on_esxi" : false,
  "pre_deploy_methods" : [],
  "method_to_run" : ["Selenium::EdgeDriver.add_new(\\\"80.0.361.57\\\"); Selenium::EdgeDriver.add_new(\\\"81.0.416.12\\\"); Browsers.call_install_for(\\\"edge\\\", \\\"80\\\", [\\\"stable\\\", \\\"beta\\\", \\\"dev\\\"], false)"],
  "revert_method" : [],
  "platform_testing" : false,  
  "platform_testing_folder" : "platform-testing2",
  "testing_level" : "sanity",  
  "terminal_deploy_branch":"edge80", 
  "esxiDeploy_branch":"master",
  "num_forks" : 150,
  "resume" : false, 
  "auto_resume" : true,
  "reboot" : false, 
  "blocking" : true,
  "snapshot_create" : false,
  "temp_snapshot" : false,
  "revert_to_oldest" : false,  
  "test_deploy_count" : 0,
  "cleanup" : false,
  "email_platform" : true,
  "db_name" : "deploy3",
  "db_pass" : "",  
  "iplist" : [  
  ],
  "is_prod" : 0,
  "env" : "callbacks-stagplatform.bsstag.com", 
  "timeout" : 20,  
  "aggressive_blocking": 22,
  "terminal_types" : ["all"],  
  "region": ["all"],  
  "sub_region": ["all"], 
  "force_stop": true, 
  "check_vm_corrupt": false,
  "reset_keys" : false,  
  "version_update" : false,  
  "manual_version_update" : false,
  "history_update" : false,  
  "block_on_error" : true,  
  "winphone": false,  
  "pre_deploy_cleanup" : true, 
  "keys_path": "/tmp/keys.yml",
  "params_file": ""
}
```
`pd dlpmac.json`

[Check Deployment deploy1 DB]("http://deploy.bsstag.com/deploy_status/1")

[Check Deployment deploy2 DB]("http://deploy.bsstag.com/deploy_status/2")

[Check Deployment deploy3 DB]("http://deploy.bsstag.com/deploy_status/3")

[Deploy Query]("https://deploy.bsstag.com/deploy_query")

`SELECT * from terminals_mac order by deployed`

## 

# WIN
```
cp deploy_params_win.json.sample dplwin.json
vim dplwin.json
```
## JSON copy:
```

```

