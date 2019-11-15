# ledpi4

## docker run
```
docker run -d -v /dev:/dev --name name -p 5994:5994 ledpi4:tag     
```
doker image: https://hub.docker.com/r/agrasagar/ledpi4     
#### example : docker run -d -v /dev:/dev --name tryMe -p 5994:5994 ledpi4:v1

## app usage
check swagger doc.     

run webserver using command:     
```
python app.py (it will run webserver on localhost on port 6994 on PI)     
then go to http://0.0.0.0:6994/swagger/     
```
