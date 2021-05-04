Playing with digital signal processing (DSP) using the pyo library (http://ajaxsoundstudio.com/pyodoc).

In this repo, the environment.yml file has been included to help with conflicts.  To utilize it:
* Install Anaconda
* Create a environment `conda create -n pyautogui_demo`
* Activate that environment `conda activate pyautogui_demo`
* Create a directory for this repository to be cloned to: `New-Item  ~\repos\pyautogui_demo -ItemType Directory; cd ~\repos\pyautogui_demo`
* Clone this repo
* Execute environment.yml `conda env update --name pyautogui_demo --file environment.yml`
* Run `python ./pyautogui_demo.py`
* Use the first part to find the coordinates of the piano keys
* Hit control-C to exit pyautogui.pixel and start the game
