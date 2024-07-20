Command to start server: 
```bash
nohup python manage.py runserver 0.0.0.0:8000 >> comender.log &
```

Command to see if server is running (list PIDs for Django)
```bash
lsof -i:8000
```

Stop server (kill al Django processes on port 8000)
```bash
kill $(lsof -t -i:8000)
```
see last 50 lines of server log
```bash
tail -n 50 codemender.log
```

trail server log file in real time
```bash
tail -f codemender.log
```
