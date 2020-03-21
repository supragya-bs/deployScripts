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

