getting started : 


you have here the Jenkins file for your ci/cd , which includes app.py file a docker file for that app , with the neccessery reqierments.
and the helm chart for that app.

for start using it u need to have:
1.eks cluster app and running with nodes
2.jenkins server up and running 
3.a node that can control the eks cluster (u can configure it by downloading aws-cli kubectl and iam-authanticator and configure your cred)
4.you need to configure your jenkins with cred to ssh server (the server that controls the eks)




#creating eks:

