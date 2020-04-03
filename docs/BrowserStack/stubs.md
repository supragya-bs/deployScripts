# quick .bashrc local

```bash
alias s_dplmac="ssh app@deploy.bsstag.com"
alias s_push="git add --all; git commit -m \"Minor update\"; git push origin master;"
alias s_dirty="cat lib/browsers.json | grep \"\\\"dirty\\\": \\\"11\\\"\" -B 5 --color=auto"
```

# quick .bashrc deploymachine

```bash
alias s_pull="cd ~/supragya/; git pull; bash ~/supragya/scripts/setal.sh; cd -;"
alias s_dinfo="bash ~/supragya/scripts/deployinfo.sh"
alias s_mjson="coolcat ~/supragya/json/dplmac.json"
alias s_wjson="coolcat ~/supragya/json/dplwin.json"
alias s_mdpl="pd ~/supragya/json/dplmac.json"
alias s_wdpl="pd ~/supragya/json/dplwin.json"
```

# Stubs

### CMD to remember (test)

| CMD                              | DESC                                                      |
| -------------------------------- | --------------------------------------------------------- |
| s_dinfo                          | Deploy machine folder and DB info                         |
| s_addm `env IP LIST`             | Add mac Terminals to env                                  |
| s_addw `env IPLIST`              | Add win Terminals to env                                  |
| s_addeachm `env`                 | Add each mac Terminal type to env                         |
| s_addeachw `env`                 | Add each win Terminal type to env                         |
| s_logw `IP`                      | Start logging windows device                              |
| s_logm `IP`                      | Start loggin mac device                                   |
| s_ipninja                        | ipNinja invoke                                            |
| s_dirtyshow                      | Show dirty bits in `terminalDeploy`                       |
| s_dirtysetm `browserlist`        | Set only the dirty bits of browsers in browser list (Mac) |
| s_dirtysetw `browserlist`        | Set only the dirty bits of browsers in browser list (Win) |
| s_slblock `user reason 1f 3dwin` | Slack notify blocking in deploy machine                   |
| s_slrel `user reason 1f 3dwin`   | Slack notify releasing in deploy machine                  |
| s_pdm                            | Run parallel deploy with Mac's JSON (verifies first)      |
| s_pdshowm                        | Show Mac's parallel deploy JSON                           |
| s_pdw                            | Run parallel deploy with Win's JSON (verifies first)      |
| s_pdshoww                        | Show Win's parallel deploy JSON                           |
| s_pull                           | Fast git pull on deploy machine                           |
| s_push                           | Fast git origin push                                      |

### Show what's going on in each deploy folder

```bash
echo "--------- DEPLOY FOLDERS -----------"
cd ~/deploy;  printf "Deploy1: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy2; printf "Deploy2: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy3; printf "Deploy3: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy4; printf "Deploy4: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy5; printf "Deploy5: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy6; printf "Deploy6: "; git rev-parse --abbrev-ref HEAD;
echo "--------- DEPLOY DBs -----------"
printf "\tDBTYPE\tTOTAL\tDONE\tREM\tTIME\tLOCK\n"
printf "WINDOWS\n"
printf "\tWinDB1: "
curl -u admin:pq8CcXo9qhd5Yd9bVE "http://deploy.bsstag.com/deploy_status/1" > ~/tmp_deploy_db_web_response 2>/dev/null;
grep Windows ~/tmp_deploy_db_web_response -A 18 | awk  -F '[<>]' '/<td / { gsub(/<b>/, ""); sub(/ .*/, "", $3); printf $3; printf "\t"; } '
[ -f "/tmp/deploy1_win.lock" ] && printf "YES" || printf "NO"
echo " "
printf "\tWinDB2: "
curl -u admin:pq8CcXo9qhd5Yd9bVE "http://deploy.bsstag.com/deploy_status/2" > ~/tmp_deploy_db_web_response 2>/dev/null;
grep Windows ~/tmp_deploy_db_web_response -A 18 | awk  -F '[<>]' '/<td / { gsub(/<b>/, ""); sub(/ .*/, "", $3); printf $3; printf "\t"; } '
[ -f "/tmp/deploy2_win.lock" ] && printf "YES" || printf "NO"
echo " "
printf "\tWinDB3: "
curl -u admin:pq8CcXo9qhd5Yd9bVE "http://deploy.bsstag.com/deploy_status/3" > ~/tmp_deploy_db_web_response 2>/dev/null;
grep Windows ~/tmp_deploy_db_web_response -A 18 | awk  -F '[<>]' '/<td / { gsub(/<b>/, ""); sub(/ .*/, "", $3); printf $3; printf "\t"; } '
[ -f "/tmp/deploy3_win.lock" ] && printf "YES" || printf "NO"
echo " "
printf "MAC\n"
printf "\tMacDB1: "
curl -u admin:pq8CcXo9qhd5Yd9bVE "http://deploy.bsstag.com/deploy_status/1" > ~/tmp_deploy_db_web_response 2>/dev/null;
grep "Mac Terminal" ~/tmp_deploy_db_web_response -A 18 | awk  -F '[<>]' '/<td / { gsub(/<b>/, ""); sub(/ .*/, "", $3); printf $3; printf "\t"; } '
[ -f "/tmp/deploy1_mac.lock" ] && printf "YES" || printf "NO"
echo " "
printf "\tMacDB2: "
curl -u admin:pq8CcXo9qhd5Yd9bVE "http://deploy.bsstag.com/deploy_status/2" > ~/tmp_deploy_db_web_response 2>/dev/null;
grep "Mac Terminal" ~/tmp_deploy_db_web_response -A 18 | awk  -F '[<>]' '/<td / { gsub(/<b>/, ""); sub(/ .*/, "", $3); printf $3; printf "\t"; } '
[ -f "/tmp/deploy2_mac.lock" ] && printf "YES" || printf "NO"
echo " "
printf "\tMacDB3: "
curl -u admin:pq8CcXo9qhd5Yd9bVE "http://deploy.bsstag.com/deploy_status/3" > ~/tmp_deploy_db_web_response 2>/dev/null;
grep "Mac Terminal" ~/tmp_deploy_db_web_response -A 18 | awk  -F '[<>]' '/<td / { gsub(/<b>/, ""); sub(/ .*/, "", $3); printf $3; printf "\t"; } '
[ -f "/tmp/deploy3_mac.lock" ] && printf "YES" || printf "NO"
echo " "
```



## Enable TrustedInstaller and wuauserver

```bash
cd /cygdrive/c/windows/servicing
mv TrustedInstaller_absent.exe TrustedInstaller.exe
sc config trustedinstaller start= demand
net start trustedinstaller
reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\wuauserv" /v ImagePath /d "%systemroot%\\System32\\svchost.exe -k netsvcs" /t REG_EXPAND_SZ /f
sc config wuauserv obj= LocalSystem
sc config wuauserv start= demand
net start wuauserv
```

## MacOS tail logs (TODO)

```bash
cd /var/log/browserstack/
```

## Windows tail logs

```bash
cd "/cygdrive/c/users/root/~bs_stuff/log"
tail -f win_server.log win_cleanup.log
```

## Dashboard reboot MAC

```bash
ruby ~/downloadable/mac_dashboard_reboot.rb 207.254.53.41	
```

## Dirty Bits (terminalDeploy) finder

```bash
alias showdirtybits="cat lib/browsers.json | grep \"\\\"dirty\\\": \\\"11\\\"\" -B 5 --color=auto"
showdirtybits
```

## Fast Git Push master

```bash
git add --all
git commit -m "Minor update" 
git push origin master
```

## deploy commands

#### alltype_block_env

```bash
ruby browser_automation/add_terminals.rb supragya-block thor
```

#### add_win

```bash
for i in \
207.254.62.174 207.254.37.233 207.254.37.40 \
ruby ~/downloadable/add_win.rb $i callbacks-stagplatform; \
done;
```

#### add_mac

```bash
for i in \
207.254.62.174 207.254.37.233 207.254.37.40 \
ruby ~/downloadable/add_mac.rb $i callbacks-stagplatform; \
done;
```





```
- webassembly
- javascript pwa
- D3js
- https://hal-emse.ccsd.cnrs.fr/emse-01006565/file/2014_01_WP_Cattaruzza_The_Multi_Trip_Vehicle_Routing_Problem_with_Time_Windows_and_Release_Dates.pdf
- educative.io 
```

```
- joris mail - again deploy done
```

```
OWNER			WHAT		KEYNAME
PlatforKEY     infra
KEY     beta.infra
FOLDER  aws
  KEY   aws/access_key_id
  KEY   aws/secret_access_key
FOLDER  us_east
  KEY   us_east/username
  KEY   us_east/passwd
  KEY   us_east/ILO_user
  KEY   us_east/ILO_pass
FOLDER  eu_west
  KEY   eu_west/username
  KEY   eu_west/passwd
FOLDER  leaseweb
  KEY   leaseweb/username
  KEY   leaseweb/passwd
  KEY   leaseweb/us_token
  KEY   leaseweb/sydney_token
FOLDER  macminivault
  KEY   macminivault/passwd
  KEY   macminivault/portal_password
FOLDER  mumbai
  KEY   mumbai/ipmi_user
  KEY   mumbai/ipmi_pass
FOLDER  platform_testing
  KEY   platform_testing/key
  KEY   platform_testing/bs_username
  KEY   platform_testing/bs_access_key
  KEY   platform_testing/bs_user_id
KEY     admin
KEY     admin_query
KEY     deploy_region
KEY     encryption_key
KEY     post_support_check
KEY     bsadmin
KEY     www
KEY     deploy
KEY     mandrill_api_key
KEY     aws_access_key_id
KEY     aws_secret_access_key
KEY     super_pass
KEY     user_key
KEY     clone_key
KEY     graphite
KEY     zombiegraphite
KEY     zombie.bsstag.com
KEY     apple-id@browserstack.com
KEY     logs.browserstack.com
KEY     lic_server
KEY     lic_server_key
KEY     platform_jenkins_token
KEY     deploy_machine_jenkins
FOLDER  envs
  KEY   envs/www
  KEY   envs/deploy
  KEY   envs/platformdev
  KEY   envs/localdev
  KEY   envs/mobiledev
  KEY   envs/urgentci
  KEY   envs/wtf2
  KEY   envs/wtf
  KEY   envs/hulk
  KEY   envs/fu
  KEY   envs/thor
  KEY   envs/devdas
  KEY   envs/maserati
  KEY   envs/wonderwoman
  KEY   envs/shaktimaan
  KEY   envs/ci
  KEY   envs/dev
  KEY   envs/maserati1
  KEY   envs/callbacks
  KEY   envs/callbacks-devplatform
  KEY   envs/stagautomate
FOLDER  win_terminal
  KEY   win_terminal/staging_ssh
  KEY   win_terminal/staging_vnc
  KEY   win_terminal/ssh
  KEY   win_terminal/vnc_pass
KEY     level1_admin_key
KEY     esxi_password
KEY     temp_esxi_password
KEY     samson_key
KEY     insider_preview_password
KEY     terminal_vnc
KEY     statuspage_io
KEY     status_io
KEY     platform_vault_token
```

```

Teams,

We have been monitoring the data that is being pushed to zombies to the table "platform_stats" with "category" being "platform", and here are few of our findings:

1. There have been >87 kinds of data being pushed to the table under our category, many of which is not directly consumed by the platform team. Aggregating the data kinds, we find that volume of data pushed is hovering around 2,000,000 records per day to the table. At peak, this goes as high as 3,000,000 records in a 24hr window. Link to view charts.

[Put 24hr aggregate]

2. If the data that platform team currently uses is the only data that is to be considered, that amounts to a volume of 150,000 records in a 24hr window which is 5-10% of what's already being pushed.

3. Two of the kinds - namely "vid-rec-extra-time" and "local-tainted-socket-close" together constitute about 70% of the data being pushed. These we have already categorised as "Red" (see explanation in point 5).

4. Data of kind "local*" are being pushed in a high volume in general.

5. We don't have clarity on whether kinds other than the ones mentioned above are being currently in use, for this we are categorizing the kinds as follows: "Red" category are the kinds which will be not be pushed to zombies now (should be removed from code as well), "Blue" kinds are currently in question - whether they should be kept or not (your actions are required w.r.t. these kinds enumerated below in a maximum of 3 working days - tell us whether any of these kinds you still use and hence do not want them to be stopped being pushed to zombies - list the actions to be done in this link. sage' needs to be defined explicitly in terms of alerting/reporting/monitoring and does it need to still remain in zombies or could be shifted to bigquery?), "Green" ones are the ones that platform team has identified that it currently needs, which the team is looking forward to move to BigQuery, "Yellow" ones are kinds which need resolution from within the platform team.

[Put rangeen charts here]

Regards,
Supragya Raj
Software Engineer
Desktop Platform Team


video-stats-file-not-found	timeout-error-websocket	safari_driver_error	video-start-error	session-log	local-error-no-data-in-time	local-no-request-line-timeout	5555-down	5555-down-terminal	local-write-to-client-failed	event-log	machine-reachability	local-crunch-no-data-received	video-stop-error	local-luminati-failures	blocked-spam-url	local-stuck-host	geturl-request-mismatch	socket_open_7778_failed	simulator-device-not-found	timeout-error	local-could-not-connect-to-url	snapshot-jar-not-running	video-stop-error-stack	geolocation-stats	video-stats-very-large-upload-time	local-error-no-response-received	datajs-trigger-error	ip-geolocation-failed	video-stats-large-upload-time	local-request-response-mismatch	local-privoxy-error-page	local-connect-drained-socket	sql_for_nta	5555-memory-exceeded


```

