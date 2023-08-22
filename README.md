![Untitled](https://github.com/youssefshibl/bcell_clone_from_redis/assets/63800183/b1c6b4fd-4231-469b-b613-ffd6be49b062)


# Bcell Clone From Redis
### what is bcell ?
bcell is cache server which store data as key-value in Ram like redis writen by python.

### How start bcell ?
run `spawn_redis_server.sh` to start redis server
this will run python file in app/main.py , this by default run on port 6379 

### How run bcell cli to execute command 
run `spawn_bcell_cli.sh` to start bcell cli , to test bcell write in cli `PING` you will get `PONG`
```
$./spawn_bcell_cli.sh
>>ping
PONG
```