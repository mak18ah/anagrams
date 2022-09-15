Compares two words passed in and determines if passed in value is an anagram. 

To run:

```
docker run -it --rm -v $PWD:/home/project -w /home/project python:3.10.7 python anagram.py
```

Running tests:
```
docker run -it -v $PWD:/home/project -w /home/project python:3.10.7 /bin/bash -c "pip install -r requirements.txt && pytest"
```
