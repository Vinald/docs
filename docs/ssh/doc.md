# doc

```
nano ~/.ssh/config

Host vxnaid-staging
    HostName 191.21.12.3
    User ubuntu
    IdentityFile /home/vx/Credentials/Staging-server-key/key.pem

chmod 600 ~/.ssh/config

chmod 400 /home/vx/Credentials/Staging-server-key/key.pem

ssh vxnaid-staging

```
