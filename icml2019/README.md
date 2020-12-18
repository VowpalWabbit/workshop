# Real World Reinforcement Learning Workshop

### ICML 2019
[ICML session page](https://icml.cc/ExpoConferences/2019/schedule?workshop_id=1)  
Sunday June 9, 2019  
2PM - 6:30PM  
Room 104  

## Abstract
Microsoft recently announced the Azure Cognitive Service, Personalizer, aimed at democratizing real world reinforcement learning for context personalization. Its goal is to make reinforcement learning accessible to everyone, not just machine learning experts. Personalizer is the result of a successful partnership between Microsoft Research and Azure Cognitive Services aimed at rapid technology transfer and innovation.

In this workshop you will learn the theory behind contextual bandits and how this applies to content personalization. We will walk you through setting up the service, writing your first application, and optimizing the policy using offline optimization.

## Schedule

<table>
  <tr>
    <td>2PM - 3PM</td>
    <td>Introduction to reinforcement learning and contextual bandits <a href="https://github.com/VowpalWabbit/workshop/blob/master/ICML2019/01_RLIntro.pdf">(Slides)</a></td>
  </tr>
  <tr>
    <td>3PM - 3:30PM</td>
    <td>Overview of Azure Cognitive Services Personalizer <a href="https://github.com/VowpalWabbit/workshop/blob/master/ICML2019/02_PersonalizerOverview.pdf">(Slides)</a></td>
  </tr>
  <tr>
    <td>3:30PM - 4PM</td>
    <td><span style="font-style:italic">Break</span></td>
  </tr>
  <tr>
    <td>4PM - 4:30PM</td>
    <td>Hands on: Setting up SDK and writing first application <a href="https://github.com/VowpalWabbit/workshop/blob/master/ICML2019/03_SDKSetupAndCFE.pdf">(Slides)</a></td>
  </tr>
  <tr>
    <td>4:30PM - 5PM</td>
    <td>Hands on: Counterfactual evaluation and offline policy optimization</td>
  </tr>
  <tr>
    <td>5PM - 5:30PM</td>
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
    1. ```pip install azure-cognitiveservices-personalizer```
3. Paste your endpoint into [line 34 of ./demo/demo.py](https://github.com/VowpalWabbit/blob/master/ICML2019/demo/demo.py#L34)
4. Paste your key into [line 35 of ./demo/demo.py](https://github.com/VowpalWabbit/blob/master/ICML2019/demo/demo.py#L35)
5. run `python ./demo/demo.py`

## Next steps
- [Personalizer](https://azure.microsoft.com/en-us/services/cognitive-services/personalizer/)
- [Personalizer docs](https://docs.microsoft.com/en-us/azure/cognitive-services/personalizer/)
- How can personalization be integrated into what you work on day to day?

## Presenters
- John Langford
- Rodrigo Kumpera
- Alexey Taymanov
- Cheng Tan
