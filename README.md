# repoprox
Small proxy for repo and profit

## Install

### The Python script
Copy the `bin/app.py` to `/usr/local/bin/app.py` or any other location of your
own choosing, with a name of your own choosing. We do not judge.

### The Config

Copy the `etc/repoprox.conf` file to `/usr/local/etc/repoprox.conf` or as
above, to any location you would prefer. You will need to adjust for this in
the `app.py` file.

This config file specifies the path `/srv/install/proxy/` as storage for the
files downloaded.

### Systemd

For having SystemD handling of the proxy copy the `systemd/repoprox@.service`
file to  `/etc/systemd/system/` then reload systemd by running

```
$ sudo systemctl daemon-reload
```

then you can enable and start the proxy like this:
```
$ for a in $(seq 21610 21624) ; do sudo systemctl enable repoprox@$a.service ; done
$ for a in $(seq 21610 21624) ; do sudo systemctl start repoprox@$a.service ; done
```

You will need to adjust the `systemd/repoprox@.service` if you change the
location of anything above.

### Cron

To be able to recive updates to the repos we clean the files that keep
metadata for the repos, just copy the `bin/proxy.clean.sh` to
`/usr/loca/sbin/` (or any other place) and then add this to your crontab:
```
20 01 * * * /usr/local/sbin/proxy.clean.sh
```

