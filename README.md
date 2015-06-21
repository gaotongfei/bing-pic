# bing-pic-api

## How to use it?

You just clone this repo.

`git clone https://github.com/gaotongfei/get-bing-pictures-of-the-day.git`

Then install the requirements.

`pip install -r requirements.txt`

Run `python3 crawler.py`.

You can find the image in the dictory `bing_image`.

## How to download the pic daily?

Learn more about [`crontab`][1]

## Use it as your background

Just add this code in your css file

```
body {
    background-image: url("http://bimage.gaotongfei.com/bing-image");
}
```

[1]: http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5
