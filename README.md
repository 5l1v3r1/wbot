# wbot
WhatsApp Bot via WhatsAppWeb

# usage

Requirements

- python3
- firefox

If you prefere to run this project on chromium / chrome you need to get the chromiumdriver which will work as well.

In wbot.py the path to geckodriver must be set. Make sure you fill in the full path!

```python
browser = webdriver.Firefox(executable_path='C:\user\wbot\geckodriver')
```

In main.py put a send command like this:

```python
wbot.send_messages_to_contact('Charlie Chaplin', 'Hello, how are you?')
```


The Linux & Mac users can now run it by using the run.sh
```bash
$ ./run.sh
```



The Windows users can run it by calling it via python3
```cmd
python3 main.py
```

Once running a browser tab will show you a QR code which you need to scan with your phone.

Ready to go.

I am not responsible for anything you do with this bot. Be careful and be nice. Don't send Spam.

Note: This Project was initialized by Carlos Göhring @sbytex


