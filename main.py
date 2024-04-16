import subprocess as sub
import os  ,optparse
if os.geteuid()!=0:
    print("run it on the sudo")
    exit()
paser=optparse.OptionParser()
paser.add_option("-a",dest='argument',help="add argument",default=None)
(o,a)=paser.parse_args()
list_=["apt update -y ","apt upgrade -y ","apt-get update -y","apt install shh","apt install figlet-y","apt install python -y","apt install nano -y","apt install micro -y"
       ,"apt install docker.io -y ","apt install git -y","apt install hping3 -y ","apt install npm -y","apt install pip -y","apt install unrar -y","apt install wget -y ","apt install tor -y","apt install proxychains -y","apt install locate -y "]

github=["https://github.com/instaloader/instaloader.git","https://github.com/TheSpeedX/TBomb.git","https://github.com/htr-tech/zphisher.git"]

def making_dir():
        list_=["programs","git program"]
        for i in list_:
            try:
                os.mkdir(i)
            except:
                pass
def basic():
    making_dir()
    for apt_command in list_:
        sub.run(f"{apt_command}",shell=True)
    sub.run("pip install altgraph==0.17.3 appdirs==1.4.4 asttokens==2.2.1 async-generator==1.10 asyncio==3.4.3 attrs==22.2.0 backcall==0.2.0 bcrypt==4.0.1 beautifulsoup4==4.11.2 brewer2mpl==1.4.1 bs4==0.0.1 cattrs==22.2.0 certifi==2022.12.7 cffi==1.15.1 chardet==3.0.4 charset-normalizer==3.0.1 click==8.1.3 cmake==3.25.2 colorama==0.4.6 comtypes==1.1.14 contourpy==1.0.7 cryptography==39.0.1 cycler==0.11.0 DateTime==5.0 decorator==5.1.1 distlib==0.3.6 dlib==19.24.1 executing==1.2.0 fabric==3.0.0 face-recognition==1.3.0 face-recognition-models==0.3.0 filelock==3.9.0 Flask==2.2.3 fonttools==4.38.0 ggplot==0.11.5 googletrans==3.0.0 h11==0.9.0 h2==3.2.0 hpack==3.0.0 hstspreload==2023.1.1 httpcore==0.9.1 httpx==0.13.3 hyperframe==5.2.0 idna==2.10 invoke==2.0.0 ipython==8.11.0 itsdangerous==2.1.2 jedi==0.18.2 Jinja2==3.1.2 joblib==1.2.0 jsonschema==4.17.3 kiwisolver==1.4.4 libusb1==3.0.0 MarkupSafe==2.1.2 matplotlib==3.7.0 matplotlib-inline==0.1.6 MouseInfo==0.1.3 mysql-connector-python==8.0.32 nltk==3.8.1 numpy==1.24.2 opencv-contrib-python==4.7.0.68 outcome==1.2.0 packaging==23.0 pandas==1.5.3 paramiko==3.0.0 parso==0.8.3 patsy==0.5.3 pefile==2023.2.7 pickleshare==0.7.5 Pillow==9.4.0 platformdirs==3.1.0 playsound==1.3.0 plotly==5.13.0 prompt-toolkit==3.0.38 protobuf==3.20.3 psutil==5.9.4 pure-eval==0.2.2 PyAudio @ file:///F:/document/PyAudio-0.2.11-cp311-cp311-win_amd64.whl PyAutoGUI==0.9.53 pycparser==2.21 PyGetWindow==0.0.9 Pygments==2.14.0 pyinstaller==5.8.0 pyinstaller-hooks-contrib==2023.0 pyjokes==0.6.0 PyMsgBox==1.0.9 PyNaCl==1.5.0 pynput==1.7.6 pyparsing==3.0.9 pyperclip==1.8.2 pypiwin32==223 pyproject-toml==0.0.10 Py",shell=True)
def with_github():
    basic()
    os.chdir("git program")
    for git_hub in github:
        sub.run(f"git clone {git_hub}",shell=True)

def full_update():
    with_github()


if o.argument ==None:
    basic()
elif o.argument in "with github":
    with_github()
else:
    pass

