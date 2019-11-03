# http_cache_echo  
**docker-compose build** - собрать  
**docker-compose up** - запустить  

сервер на порте 2000: http://localhost:2000  

curl example:  
запись значения по ключу key  
curl -i -d "VALUE" -X POST http://localhost:2000/key  
HTTP/1.0 201 Created

получение значения по ключу key  
curl -i -X GET http://localhost:2000/key  
HTTP/1.0 200 OK  
VALUE

удаление значения по ключу key  
curl -i -X DELETE http://localhost:2000/key   
HTTP/1.0 200 OK

попробуем еще раз:  
curl -i -X DELETE http://localhost:2000/key  
HTTP/1.0 404 Not Found  

Также можно и через Postman. Например:  
http://localhost:2000/key выбрать POST в формате raw Text. Произойдет запись по ключу key с вашим текстом
