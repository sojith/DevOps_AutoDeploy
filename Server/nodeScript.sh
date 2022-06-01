pid1=$(pidof "/home/emperor/Projects/Software/node-v16.15.0-linux-x64/bin/node")
if [ ! -z $pid1  ]    
then
	echo "nodeScript.sh -- Killing node js process"
	kill $pid1
fi

echo "nodeScript.sh -- Restarting the node js process"
/home/emperor/Projects/Software/node-v16.15.0-linux-x64/bin/node /home/emperor/Projects/Devops_Project/code/App/app.js &

