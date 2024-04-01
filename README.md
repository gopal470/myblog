# myblog

A streamlit app to launch my Blog Website.

How to run and deploy the app?

```
# Open New Terminal on your Mac

# Git clone this repo
$ git clone git@github.com:gopal470/myblog.git
Cloning into 'myblog'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
$ cd myblog

# Verify the list of files. It should contain your app.py and requirements.txt
$ ls -ltr
total 24
-rw-r--r--  1 user  staff  884 Apr  1 10:40 app.py
-rw-r--r--  1 user  staff   10 Apr  1 10:40 requirements.txt
-rw-r--r--  1 user  staff   73 Apr  1 10:41 README.md
$

# Run locally and test the app
$ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.24.7.139:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog

# Open the url and verify app functionality
http://localhost:8501

# If it looks good, click "deploy" on the right upper corner.
# Choose "Streamlit Community" App.
# Create an account if you dont have one. Connect with your github repo if required.
# Then, fill the app-url, example gopalblog. And your app is launched now.
# Visit https://gopalblog.streamlit.app now and your app is ready.
```

Congratulations for successfuly launching your first Streamlit app: https://gopalblog.streamlit.app

To learn more about streamlit, visit below tutorials and documentations:
* Youtube Tutorials: [Streamlit Tutorials from Coding Is Fun](https://www.youtube.com/playlist?list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n)
* Documentation: https://streamlit.io
