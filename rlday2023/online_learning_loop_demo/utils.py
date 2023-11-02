import json

def build_vw_example(context, actions, chosen_action_index=None, reward=None,
                      prob=None, pmf=None, feedback=None):
    try:
        jsonobj = {}
        if reward is None and prob is None: # predict example
            chosen_action_index = 0
            reward = 0
            prob = 1/len(actions)
            pmf = [(index, prob) for index, _ in enumerate(actions)]
            feedback = {}

        c = context
        c['_multi'] = actions
        a = [] # 1-indexed
        p = []
        for item in pmf:
            a.append(item[0] + 1)
            p.append(item[1])
        jsonobj = {
            '_label_cost' : 0 if reward is None else -reward,
            '_label_probability': prob,
            '_label_Action': 1 + chosen_action_index,
            '_labelIndex': chosen_action_index,
            'o': [
                feedback
            ],
            'a': a,
            'c': c,
            'p': p,
        }
        return json.dumps(jsonobj)
    except Exception as e:
        print(e)
        throw(e)