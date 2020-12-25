## Technologies
* Python 3.7.6
* Flask 1.1.1  
* Docker 19.03.5

* Note: For proof of concept Python is one of the best programming language. That's why I have choosen python for this POC. I have written down a document about how to start a POC or R&D project in 2011. And published the article in 2017 in my personal blog. If you want to explore then click the link :
http://tech.mohiulalam.com/2017/03/02/how-you-will-start-your-rd-project-development/

* Note: I am using the Flask framework for the very first time

## How to Run
Install docker in your computer

build the docker image using below command
```
docker build -t tracker:latest .
```

run the docker image
```
docker run --rm --name tracker_container -it -d -p 5000:5000 tracker
```

If you want to login to the docker container to see the uploaded files in upload folder location then type
```
docker exec -it tracker_container /bin/bash
ls upload
```

If you want to stop container
```
docker container stop tracker_container
```

Now go to your brower and type http://127.0.0.1:5000/file-upload
and try to upload one of the csv or prn file format

If you want to see all the tranactions or all the source file you have been uploaded so far then type: http://127.0.0.1:5000/all-transactions

## How to Run Test
```
docker exec -it tracker_container python test_parser.py
```

## How to Run Coverage
```
(py3.7) prince@Mds-MacBook-Pro% docker run --rm --name tracker_container -it -d -p 5000:5000 tracker

256f960bd69db3d67fc4d8c1cfcfcb42c92dc31ae2f557792089e4277d1452c0
(py3.7) prince@Mds-MacBook-Pro% docker exec -it tracker_container coverage run -m unittest discover
..
----------------------------------------------------------------------
Ran 2 tests in 0.034s

OK
(py3.7) prince@Mds-MacBook-Pro% docker exec -it tracker_container coverage report -m               
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
app.py               6      0   100%
parser.py           52     22    58%   34-54, 92-93
test_parser.py      16      1    94%   21
----------------------------------------------
TOTAL               74     23    69%

```

## Sample Output
* upload file
  https://ibb.co/mbs9Z71

* file already uploaded
  https://ibb.co/XXh2cjs

* To see all the transaction
  https://ibb.co/VQ4qPNz

## Current features
* Persistence in db [ Note: right at this moment we are saving in HDD]
* unit test [ Given 2 unit test]
* coverage [ Covered few ]
* automated deployment in cloud [ circle ci intregrated ]

## Future features
* Persist in database
* Date wise search with filtering
* Auto scaling using kubernetes

## Advance features
* :-?
