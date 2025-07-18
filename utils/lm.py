# Copyright (c) Meta Platforms, Inc. and affiliates.

# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
import openai

'''
NOTE:
    Available functions:
        - call_vllm_api: using vllm self-served models
        - openai_generate: using openai models
'''
########################################################################################################
def custom_api(prompt, model, temperature=0.0, top_p=1.0, max_tokens=512, port=None):

    # raise NotImplementedError()
    return call_vllm_api(prompt, model, temperature, top_p, max_tokens, port)
    # return openai_generate(prompt, model, temperature, top_p, max_tokens)

def generate(prompt, model, temperature=0.0, top_p=1.0, max_tokens=512, port=None, i=0):

    # TODO: You need to use your own inference method
    return custom_api(prompt, model, temperature, top_p, max_tokens, port)
    # return call_vllm_api(prompt, model, temperature, top_p, max_tokens, port, i)

CUSTOM_SERVER = "0.0.0.0" # you may need to change the port

model_map = {   'meta-llama/Llama-3.1-405B-Instruct-FP8': {'name': 'llama3.1_405B',
                                                            'server_urls': [f"http://{CUSTOM_SERVER}:8000/v1"]},
                'meta-llama/Llama-3.3-70B-Instruct': {'name': 'llama3.3_70B',
                                                    'server_urls': [f"http://{CUSTOM_SERVER}:8000/v1"]},
                'meta-llama/Llama-3.1-70B-Instruct': {'name': 'llama3.1_70B',
                                                        'server_urls': [f"http://{CUSTOM_SERVER}:8000/v1"],
                                                    },
                'meta-llama/Llama-3.1-8B-Instruct': {'name': 'llama3.1_8B',
                                                        'server_urls': [f"http://{CUSTOM_SERVER}:8000/v1"],
                                                    },
                'mistralai/Mistral-7B-Instruct-v0.2': {'name': 'mistral7B',
                                                        'server_urls': [f"http://{CUSTOM_SERVER}:8000/v1"],
                                                    },
                "mistralai/Mistral-Nemo-Instruct-2407": {'name': 'Mistral-Nemo-Instruct-2407',
                                                        'server_urls': [f"http://{CUSTOM_SERVER}:8000/v1"],
                                                    },

            }
########################################################################################################

def call_vllm_api(prompt, model, temperature=0.0, top_p=1.0, max_tokens=512, port=None, i=0):
    try:
        # if port == None:
        #     port = model_map[model]["server_urls"][i]

        client = openai.OpenAI(
            base_url=f"http://localhost:8000/v1",
            api_key="NOT A REAL KEY",
        )
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user","content": prompt}],
            max_tokens=max_tokens,
            temperature=0.0,
            top_p=1.0
        )

        print(f"calling call_vllm_api with model {model}")
        print(f"prompt: {prompt}")
        print(f"response: {chat_completion.choices[0].message.content}")

        return chat_completion.choices[0].message.content
    except Exception as e:
        print(e)
        return ""

def openai_generate(prompt, model, temperature=0.0, top_p=1.0, max_tokens=512):
    try:
        # Create a client object
        client = openai.OpenAI(
            api_key="NOT A REAL KEY",
            base_url="http://localhost:8000/v1"
        )
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.0,
            top_p=1.0
        )

        print(f"calling openai_generate with model {model}")
        print(f"prompt: {prompt}")
        print(f"response: {chat_completion.choices[0].message.content}")

        return chat_completion.choices[0].message.content
    except Exception as e:
        print(e)
        return ""
