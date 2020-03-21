# Ops Links

- [Desktop Board](https://browserstack.atlassian.net/secure/RapidBoard.jspa?rapidView=59&projectKey=PLAT&selectedIssue=PLAT-2427)

- [Ops Etiquette Confluence](https://browserstack.atlassian.net/wiki/spaces/ENG/pages/1182761036/Desktop+Deploy+Etiquette)

- [DataCenter Point of Contacts](https://docs.google.com/spreadsheets/d/1cNSMVs_7N2TarSOucanksDfjCuaDsZ6CLZH_iv7Bakg/edit#gid=0)

- [MacStadium Portal](http://portal.macstadium.com/) with pswd       browserstack      UmAjXVhblVcO

- OPS Ticket format

  ```
  Deploy method: 
  Deploy branch: 
  Terminal deploy branch: (take a master merge and encrypt the branch)
  Deploy PR: (needs to be approved)
  Terminal deploy PR: (needs to be approved)
  Terminal types: 
  QA Approved: (yes/no)
  ```

- Cloning email

  ```
  Please clone the following machines (type mac-catalina):
  208.52.145.219
  208.52.145.198
  208.52.145.222
  
  Clone Source - 185.44.130.179
  Please use the following credentials
  Username: ritesharora
  Password: c10n3s0urc3
  ```

  

  # Queries

  Deploy BSSTAG passwd: w1EGU0v1tjUwZfBT4Gy6Cbn2kwA

  | Browser | WHAT?                                                        | QUERY                                                        |
  | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | Saf     | [Deploy Query](https://deploy.bsstag.com/deploy_query) failed machine list | SELECT * FROM terminals_windows WHERE deployed=-2            |
  | Saf     | [Deploy Query](https://deploy.bsstag.com/deploy_query) failed machine logs | SELECT * from exception_logs where ip in ("185.44.131.72") order by created_at desc |
  | Chr     | [Zombie sl_run_query](https://zombie.browserstack.com/admin/sl_run_query?method=post) Windows PROD state | SELECT count(*) as c, genre, state, instance_id from terminals where os like 'win%' group by state, genre, instance_id order by c DESC |
  | Chr     | [Zombie sl_run_query](https://zombie.browserstack.com/admin/sl_run_query?method=post) Mac PROD state | select count(*) as c, genre, state, instance_id from terminals where os like 'mac%' group by state, genre, instance_id order by c DESC |
  | Saf     | [Deploy Query](https://deploy.bsstag.com/deploy_query) Update deployed_state | UPDATE terminals_mac SET deployed=10 WHERE ip in ("208.52.157.71") |

# Stubs

## Terminal Deploy

```
for i in 207.254.75.91; do ruby terminal_deploy.rb mac $i "'Method'"; done;
```

### TD - PreClone

```
for i in 207.254.75.107; do ruby terminal_deploy.rb mac $i "'Setup.pre_clone'"; done;
```

### TD - PostClone

```
for i in 208.52.145.219 208.52.145.40; do ruby terminal_deploy.rb mac $i "'Setup.post_clone'"; done;
```

### Mac Dashboard Reboot

```
for i in 207.254.75.91; do ruby mac_dashboard_reboot.rb $i; done;
```

### Mac Create Space

```
for i in 185.44.129.41; do 
echo "------" && mssh $i "sudo chown ritesharora /mnt/soft/.old_logs && sudo rm -rf /mnt/soft/.old_logs/2020-01-* && sudo rm -rf /mnt/soft/.old_logs/2020-02-0* && sudo rm -rf /mnt/soft/.old_logs/2020-02-1* && sudo rm -rf /mnt/soft/.old_logs/2020-02-20 && sudo rm -rf /mnt/soft/.old_logs/2020-02-21 && sudo rm -rf /mnt/soft/.old_logs/2020-02-22 && sudo rm -rf /mnt/soft/.old_logs/2020-02-23 && sudo rm -rf /mnt/soft/.old_logs/2020-02-24 && sudo rm -rf /mnt/soft/.old_logs/2020-02-25 && sudo chown root /mnt/soft/.old_logs && sudo df -h" && echo "done"; done; 
```

### Mac force block machine

```
for i in 207.254.75.91 207.254.75.9; do ruby block_terminals.rb $i www supragya_reason y; done;
```

#### Grep IP addresses

````
grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}'
````

#### Delete Windows VMs from prod

```
for i in 208.52.145.40 208.52.145.219; do echo $i && ruby delete_ip.rb $i www ttype_mismatch; done;
```

#### Add mac

```
for i in 208.52.145.40 208.52.145.219; do echo $i && ruby add_mac.rb $i www; done;
```

#### Release terminals back to prod

```
for i in 216.126.44.87; do echo "------" && echo $i && ruby release_terminals.rb $i www; done; 
```

#### copy2san

```
bundle exec ruby copy2san.rb copy2san_params.json
```

#### Open vnc

```
for i in 185.44.131.152; do open vnc://hello:ew4cXP@$i:6001; done;
```

### Cleanup on mac haath se

```
/usr/bin/thin -R /usr/local/.browserstack/cleanup_config.ru -p 45680 --stats /stats --threaded start &
```

```
https://browserstack.atlassian.net/wiki/spaces/ENG/pages/24203399/Desktop+Platform+Basic+Info

```





# Scratchpad

```
for i in 185.44.130.192 185.44.131.145  185.44.131.62  185.44.131.64 185.44.131.146 185.44.130.195; do echo $i && chkmac $i; done;
```

```
for i in 208.52.180.227 185.44.131.72 185.44.131.7 185.44.131.88 185.44.131.152; do echo $i && ping $i -c 2 | grep loss; done;
```

```
for i in 185.44.131.72 185.44.131.7 185.44.131.88; do ruby terminal_deploy.rb mac $i "'Code.code_update'"; done;
```

```
{
  "json_version" : 10,
  "deployer" : "Supragya",
  "os" : "mac",
  "deploy_on_esxi" : false,
  "run_only_once_on_esxi" : false,
  "pre_deploy_methods" : [],
  "method_to_run" : ["mnt_folder_sanity"],
  "revert_method" : [],
  "platform_testing" : false,
  "platform_testing_folder" : "platform-testing2",
  "testing_level" : "sanity",
  "terminal_deploy_branch":"",
  "esxiDeploy_branch":"master",
  "num_forks" : 150,
  "resume" : false,
  "auto_resume" : true,
  "reboot" : false,
  "blocking" : false,
  "snapshot_create" : false,
  "temp_snapshot" : false,
  "revert_to_oldest" : false,
  "test_deploy_count" : 0,
  "cleanup" : false,
  "email_platform" : true,
  "db_name" : "deploy2",
  "db_pass" : "",
  "iplist" : [
  ],
  "is_prod" : 1,
  "env" : "www.browserstack.com",
  "timeout" : 20,
  "aggressive_blocking": 22,
  "terminal_types" : ["cat"],
  "region": ["all"],
  "sub_region": ["all"],
  "force_stop": true,
  "check_vm_corrupt": false,
  "reset_keys" : false,
  "version_update" : false,
  "manual_version_update" : false,
  "history_update" : true,
  "block_on_error" : true,
  "winphone": false,
  "pre_deploy_cleanup" : true,
  "keys_path": "/tmp/keys.yml",
  "params_file": ""
}
```

```
for i in 185.200.101.155 103.126.7.9 103.126.7.20 103.126.7.26 103.126.7.22 103.126.7.21 103.126.7.16 103.126.7.18 103.126.7.24 103.126.7.28 103.126.7.30 103.126.7.35 103.126.7.32 103.126.7.38 103.126.7.37 103.126.7.33 103.126.7.39 103.126.7.36; do echo "---------------------------------------" && echo $i && ping $i -c 2 | grep loss && essh $i  "vim-cmd vmsvc/getallvms"; done;
```

```
&& essh $i  "vim-cmd vmsvc/getallvms"
```

```

```

```
185.44.131.72
185.44.131.7
185.44.131.88
```

```
for i in 185.44.131.72 185.44.131.7 185.44.131.88; do ruby block_terminals.rb $i www selenium_plist_missing_dst y; done;
```

```
for i in 208.52.180.223; do ruby terminal_deploy.rb mac $i "'Setup.pre_clone'"; done;
```

```
for i in 208.52.180.227; do ruby block_terminals.rb $i www unpingable_machine y; done;
```

```
Test deploy
TPM
esxi
DC tickets

```

```

## Known edge cases:

```



```
["sie", "185.200.103.18"]
["sie", "185.200.103.21"]
["hs", "185.200.103.59"]
["hs", "185.200.103.56"]
["hs", "185.200.103.58"]
["hs", "185.200.101.131"] 


Sources:
185.200.103.193 - hs
46.249.62.75 - sie
```

```
for i in 185.200.103.193 46.249.62.75; do ruby terminal_deploy.rb mac $i "'Setup.pre_clone'"; done;
```

```
for i in 185.200.101.131; do ruby block_terminals.rb $i www old_private_network y; done;
```

