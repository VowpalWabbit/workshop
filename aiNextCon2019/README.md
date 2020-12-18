# Real World Reinforcement Learning Workshop

### AI NEXTCon 2019
Thursday July 25, 2019  
9:00AM - 12:00PM  

Address:  
Galvanize NYC (2nd floor)  
303 Spring St, New York, NY 10013


## Abstract
Microsoft recently announced the Azure Cognitive Service, Personalizer, aimed at democratizing real world reinforcement learning for content personalization. Its goal is to make reinforcement learning accessible to everyone, not just machine learning experts. Personalizer is the result of a successful partnership between Microsoft Research and Azure Cognitive Services aimed at rapid technology transfer and innovation.

In this workshop you will learn the theory behind contextual bandits and how this applies to content personalization. We will walk you through setting up the service, writing your first application, and optimizing the policy using offline optimization.

## Schedule

<table>
  <tr>
    <td>9:00AM - 9:45AM</td>
    <td>Introduction to reinforcement learning and contextual bandits <a href="https://github.com/VowpalWabbit/workshop/tree/master/aiNextCon2019/01_RLIntroduction.pptx">(Slides)</a></td>
  </tr>
  <tr>
    <td>9:45AM - 10:15AM</td>
    <td>Overview of Azure Cognitive Services Personalizer <a href="https://github.com/VowpalWabbit/workshop/tree/master/aiNextCon2019/02_PersonalizerOverview.pptx">(Slides)</a></td>
  </tr>
  <tr>
    <td>10:15AM - 10:30AM</td>
    <td><span style="font-style:italic">Break</span></td>
  </tr>
  <tr>
    <td>10:30AM - 11:10AM</td>
    <td>Hands on: Setting up SDK and writing first application <a href="https://github.com/VowpalWabbit/workshop/tree/master/aiNextCon2019/03_sdkSetup.pptx">(Slides)</a></td>
  </tr>
  <tr>
    <td>11:10AM - 11:30AM</td>
    <td>Hands on: Counterfactual evaluation and offline policy optimization <a href="https://github.com/VowpalWabbit/workshop/tree/master/aiNextCon2019/04_CFE.pptx">(Slides)</a></td>
  </tr>
  <tr>
    <td>11:00AM - 12:00PM</td>
    <td>Wrap-up and Q&amp;A</td>
  </tr>
</table>

## Workshop Instructions
1. [Create free Azure/Microsoft account](https://azure.microsoft.com/en-us/free/)
2. Provision free instance of Personalizer
    1. Go to [Azure Portal](https://portal.azure.com)
    2. Search for "Cogitive Services"
    3. On Cognitive Services page click "Add"
    4. Search for "Personalizer (Preview)" and click "Create"
3. Install Python Client
   ```pip install azure.cognitiveservices.personalizer```
3. Paste your endpoint into [line 34 of ./demo/demo.py](https://github.com/VowpalWabbit/workshop/blob/master/demo/demo.py#L34)
4. Paste your key into [line 35 of ./demo/demo.py](https://github.com/VowpalWabbit/workshop/blob/master/demo/demo.py#L35)
5. run `python ./demo/demo.py`

## Next steps
- [Personalizer](https://azure.microsoft.com/en-us/services/cognitive-services/personalizer/)
- [Personalizer docs](https://docs.microsoft.com/en-us/azure/cognitive-services/personalizer/)
- How can personalization be integrated into what you work on day to day?

## Presenters
- John Langford
- Rodrigo Kumpera
- Rajan Chari
- Pavithra Srinath
