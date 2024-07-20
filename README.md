Command to start server: 
```
nohup python manage.py runserver 0.0.0.0:8000 >> comender.log &
```

Command to see if server is running (list PIDs for Django)
```
lsof -i:8000
```

Stop server (kill al Django processes on port 8000)
```
kill $(lsof -t -i:8000)
```
see last 50 lines of server log
```
tail -n 50 comender.log
```

trail server log file in real time
```
tail -f comender.log
