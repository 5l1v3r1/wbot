# wbot
WhatsApp Bot via WhatsAppWeb

# usage

Requirements

- python3
- firefox

In wbot.py the path to geckodriver must be set. Make sure you fill in the full path!

```
browser = webdriver.Firefox(executable_path='C:\user\wbot\geckodriver')
```

In main.py put a send command like this:

```
wbot.send_messages_to_contact('Charlie Chaplin', 'Hello, how are you?')
```


The Linux & Mac users can now run it by using the run.sh
```
$ ./run.sh
```



The Windows users can run it by calling it via python3
```
python3 main.py
```

Once running a browser tab will show you a QR code which you need to scan with your phone.

Ready to go.

I am not responsible for anything you do with this bot. Be careful and be nice. Don't send Spam.


