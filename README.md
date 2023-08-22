![Untitled](https://github.com/youssefshibl/bcell_clone_from_redis/assets/63800183/b1c6b4fd-4231-469b-b613-ffd6be49b062)


# Bcell Clone From Redis
### 🚧 what is bcell ?
bcell is cache server which store data as key-value in Ram like redis writen by python.

### 🚧 How start bcell ?
run `spawn_redis_server.sh` to start redis server
this will run python file in app/main.py , this by default run on port 6379 

### 🚧 How run bcell cli to execute command 
run `spawn_bcell_cli.sh` to start bcell cli , to test bcell write in cli `PING` you will get `PONG`
```
$./spawn_bcell_cli.sh
>>ping
PONG
>>ping test
test
```
### 🚀 Bcell Command
|               Command                |       Description       |     Response     |
| :----------------------------------: | :---------------------: | :--------------: |
|                 PING                 |     Test bcell cli      |       PONG       |
|              PING TEST               |     Test bcell cli      |       TEST       |
|             ECHO "ahmed"             |       echo string       |     "ahmed"      |
| SET KEY VALUE<br />SET comment ahmed |   set value with key    |        OK        |
|       GET KEY<br />GET comment       |    get value by key     | VALUE<br />ahmed |
|    DELETE KEY<br />DELETE comment    |    delete raw by key    |        OK        |
|     EXIST KEY<br />EXIST comment     |   check if key exist    | TRUE<br />FALSE  |
|                FLUSH                 |     delete all data     |        OK        |
|                 SAVE                 | take snapshot from data |        OK        |

### 🗒️  Get snapshot from data 

when run  `SAVE` this command take snapshot from data and store it in `data.json` file in `data` directory when server start it take data from this file and save it in memory 