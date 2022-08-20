# melancholia

## install required stuff
- install [puredata](http://msp.ucsd.edu/software.html)
- `pip install -r requirements.txt`

## usage of simple:
1. open the puredata patch
2. call the python script with `python simple-client.py <some string>`
3. see how the string was printed in puredata's console

## usage of oscillator:
1. open the oscillator-receiver puredata patch
2. call the python script without arguments `python oscillator-client.py`
3. the slider will bounce back and forth until the script is interrupted

## System Diagram
![system diagram](https://github.com/maxiestudies/melancholia/blob/master/docs/system_diagram.png)

## Description of the pieces
[org file](https://github.com/maxiestudies/melancholia/blob/master/docs/doc.org)
