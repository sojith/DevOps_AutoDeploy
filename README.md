# AutoDeployment

This project is meant to show how one can automatically deploy any code commits into a test env server

1) https://github.com/sojith/DevOps/blob/main/App/app.js - This is a simple NodeJS script used to host a page. The github repo on which this is hosted has an outgoing webhook. Any commits in this repo leads to the webhook sending a post message to an endpoint (this endpoint is mentioned in the point below)

2) _./myserver.py_ - This python script hosts the endpoint which recieves messages from webhooks of the repo mentioned above. This message will contain the details on the commits i.e. whether files have been Added, Modifed or Removed. In case of any commits, this python script downloads the repo in point 1 into the server. It then restarts the nodejs server by running _./nodeScript.sh_. The script then proceeds to run a smoke test by calling a Selenium test case (_./sojith/smoketest_selenium.py_)

 
