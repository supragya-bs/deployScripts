# BrowserStack

# Links



## Staging Platform

To select only a particular terminal, use `Constants.custom_terminal=“<IP>”`

## Terminal access

### scp

`scp -P 4022 root@185.129.69.108:/home/Administrator/ieframe_sys32.dll .`

### Cygwin access

`scp -P 4022 [root@185.129.69.108](mailto:root@185.129.69.108)`

### Deploy access

[http://deploy.bsstag.com/admin/terminals](http://deploy.bsstag.com/admin/terminals)

Username: `admin`

Passwd: `pq8CcXo9qhd5Yd9bVE`

### Change password of admin

`net user Administrator passwd`

## Log location

`/cygdrive/c/Users/root/~bs_stuff/log`

`tail -200 win_cleanup.log | grep sync_time`

## VBScript run

`assoc .vbs=VBSFile`

## OPs KT

2 OPs:

1. Main OPs
2. Aux OPs

    [Untitled](https://www.notion.so/1b3b6368ffb34f06b61c085c63bc1d34)

## ENV

1. Prod
2. Stag
3. Deploy machine (deploy.browserstack.com)/(deploy.bsstag.com) ssh pub in all terminals
4. deploy repo cloned eight times... one of the folders to be used
5. Check `/etc/cron.d/app_platform`
6. Check in deploy terminals `deploy.bs.com/server.rb`

## Support Ops

### Deploy machine

`ssh app@deploy.bsstag.com`