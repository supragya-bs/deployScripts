

# Dashboard discussion

## Dashboard idea in general

- Sucks 
  - Nobody wants to write it - HTML, firefighting mode
  - No effect visible till made
  - Not extensible - html again
  - I want to use grep with it
- I want it on deploy machine
- I want to log it and easily query



# (￣^￣)ゞ HELMSMAN

## Directory Structure

```
version.info
logs/
	dynamoDB
db/
	hookbased/
    Mac/Win Diff
    ESXi Utilisation
    Open Ports (NMAP Scan)
    chkbrowser
core/
	zombies_helper
	deploy_query
	sl_run_query
	ipninja
scripts/
	db/
		mdiff
		wdiff
		eutil
		portstat
		chkbrowser
	p2s 	- prod2stag
	s2p 	- stag2prod
	gm 		- getmachine <count> <os> <subregion>
	precb	- precloneblk <IP> | <os> <subregion>
	postcb - postcloneunblk <IP>
	dpls 	 	- deploystate <db>
	dplm1  - deploy -1 report [ dplmin1 <os> <db> ]
	dplm2  - deploy -2 report [ dplmin1 <os> <db> ]
	dminf - deploy machine information
	dbln - deployblocknotify <reason> <folder> <db> (slackbot integration)
	dreln -  
	mdr 	- mcdreboot <IP>
	ipn		- ipninja
	eaddm  - env add mac
	eaddw. - env add w
	mach	- mac health report (ping, chkmac, chkver)
	winh*  - windows health report
	iiddist - instance_id distribution
	smkpng*
	lck - lock info
	bhlth - Browser's health on prod
	dhcplinfo
```

```
(￣^￣)ゞ
```

