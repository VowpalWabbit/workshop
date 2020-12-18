# Real World Reinforcement Learning with Vowpal Wabbit

### NeurIPS 2019
Sunday December 8, 2019  

## Abstract
Reinforcement learning is increasingly being used to solve real world personalization and optimization scenarios, with online, sample efficient algorithms such as Contextual Bandits. Companies such as Netflix [(https://medium.com/netflix-techblog/artwork-personalization-c589f074ad76)](https://medium.com/netflix-techblog/artwork-personalization-c589f074ad76) and The New York Times [(https://open.nytimes.com/how-the-new-york-times-is-experimenting-with-recommendation-algorithms-562f78624d26)](https://open.nytimes.com/how-the-new-york-times-is-experimenting-with-recommendation-algorithms-562f78624d26) are using Contextual Bandits to personalize content and optimize engagement. Across multiple deployments Microsoft uses Contextual Bandits, and recently released the [Personalizer Azure Cognitive Service](http://aka.ms/personalizer) which is the world's first real world reinforcement learning service.

[Vowpal Wabbit](https://vowpalwabbit.org) is an open source machine learning library, extensively used by industry, and is the [first public terascale learning system](https://arxiv.org/abs/1110.4198). It provides fast, scalable machine learning and has unique capabilities such as learning to search, active learning, contextual memory, and extreme multiclass learning. It has a focus on reinforcement learning and provides production ready implementations of Contextual Bandit algorithms. Vowpal Wabbit sees significant innovation as a research to production vehicle for Microsoft Research.

Come and learn about reinforcement learning, Vowpal Wabbit, and applying contextual bandits to problems using Vowpal Wabbit

## Schedule

- What is Vowpal Wabbit?
- New developments and what’s in the pipeline
- What are Contextual Bandits?
- Real world usage of Contextual Bandits and Vowpal Wabbit
- VW + Python
- VW + Python + Contextual Bandits 

## Slides
- [Introduction](https://github.com/VowpalWabbit/workshop/blob/master/neurips2019/intro.pdf)
- [Contextual Bandits](https://github.com/VowpalWabbit/workshop/blob/master/neurips2019/contextual_bandits.pdf)
- [Personalizer](https://github.com/VowpalWabbit/workshop/blob/master/neurips2019/personalizer.pdf)
- [VW on Spark](https://github.com/VowpalWabbit/workshop/blob/master/neurips2019/VW_on_Spark.pdf)

## Resources
- [https://vowpalwabbit.org](https://vowpalwabbit.org)
- [Classification notebook](https://mybinder.org/v2/gh/VowpalWabbit/jupyter-notebooks/master?filepath=VW%20classification%20tutorial.ipynb)
- [Content personalization tutorial](https://vowpalwabbit.org/tutorials/cb_simulation.html) [(Jupyter notebook)](https://mybinder.org/v2/gh/VowpalWabbit/jupyter-notebooks/master?filepath=Simulating_a_news_personalization_scenario_using_Contextual_Bandits.ipynb)
