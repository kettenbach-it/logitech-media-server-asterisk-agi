# AGI for controlling the Logitech Media Server from Asterisk

## Requirements
You will need at least Python 3.7 and virtual env (python3 -m venv venv) to run this.

## Usage in Asterisk
Here's an example how you can use this AGI in an Asterisk macro:

```
[macro-LMSToggle]
exten => s,1,AGI(lms.agi.py,00:04:20:23:a4:61,mode)
exten => s,n,NoOp(LMS Status: ${LMSSTATUS})
exten => s,n,ExecIf($["${LMSSTATUS}" = "play"]?AGI(lms.agi.py,00:04:20:23:a4:61,pause))
```


## References

### Source Code
Can be found on [GitHub](https://github.com/kettenbach-it/logitech-media-server-asterisk-agi.git)


## License
GNU AGPL v3

Fore more, see [LICENSE](LICENSE)

