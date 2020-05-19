# Autonomous Marketplace Device

The objective of this project is to build a decision making process for a device registered to the Industry Marketplace to automatically choose the best service requests based on matching eCl@ass capabilities.

Please read instructions at https://www.hackster.io/naveenbskumar/autonomous-marketplace-device-adebf3 to setup environment.

The idea is to use the sent or rejected proposal data which were decided by human agent in the recent past. For this exercise we selected Decision Trees which are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.

We have considered Drone Connectivity Provioning service as an example.

The full example code which uses the model for decision can be found at industry-marketplace-python-helper/service_provider.py. 

The request can be sent using UI by selecting "Drone Connectivity Provision" operation or running industry-marketplace-python-helper/service_requester.py with drone_connectivity_provision parameter.


