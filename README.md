# t4b-tools

These are two scripts from [John Schember](https://nachtimwald.com) originating from one of their post :  
[https://nachtimwald.com/2010/01/13/cybook-t4b-format-specification/](https://nachtimwald.com/2010/01/13/cybook-t4b-format-specification/)
They were fixed, adapted to work with python 3 and now take optionals width and height arguments.  

## t4b

`t4b` is the picture format used on Bookeen's Cybook Orizon, for thumbnails (.thn), screensaver images (.bin, .t4b), etc.
These are 4bpp greyscale images.

## Usage 

Converting an image to t4b :

```python
python img2t4b.py input.png output.bin 600 800
```

Converting a t4b/bin file to pgm :

```python
python t4b2pgm.py input.bin output.pgm 600 800
```

If width/height arguments are not provided, the scripts default to 96x144, the default thumbnail size.

Original image :  
![Original image](https://schnappy.xyz/assets/noidea.jpg)  

Image converted to bin, then back to pgm :  
![PGM greyscale image](https://schnappy.xyz/assets/noidea_gs.jpg)  
[PGM file](https://schnappy.xyz/assets/noidea.pgm)  
