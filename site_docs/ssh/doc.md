# doc

```
nano ~/.ssh/config

Host vxnaid-staging
    HostName 13.247.88.119
    User ubuntu
    IdentityFile /home/vx/IDI/IDI/Credentials/Staging-server-key/main-key.pem

chmod 600 ~/.ssh/config

chmod 400 /home/vx/IDI/IDI/Credentials/Staging-server-key/main-key.pem

ssh vxnaid-staging

```
