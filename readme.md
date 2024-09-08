
# problem

As said in https://stackoverflow.com/a/57801848 glibc bufferes stdout differently with or without a TTY attached.

In this repository you see that a python program does not print(..) properly.

There are 3 possible solutions:

- add a TTY to the container
- start python with -u
- use flush=True on all print(...)

You can find all of the possible solutions commented out in this project

# how to send a message to the queue?

```bash
mosquitto_pub -h localhost -p 1883 -t "test/topic" -m "Hello from curl"
```
