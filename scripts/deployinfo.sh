echo "--------- DEPLOY FOLDERS -----------"
cd ~/deploy;  printf "Deploy1: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy2; printf "Deploy2: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy3; printf "Deploy3: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy4; printf "Deploy4: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy5; printf "Deploy5: "; git rev-parse --abbrev-ref HEAD;
cd ~/deploy6; printf "Deploy6: "; git rev-parse --abbrev-ref HEAD;
echo "----------- DEPLOY DBs -------------"
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