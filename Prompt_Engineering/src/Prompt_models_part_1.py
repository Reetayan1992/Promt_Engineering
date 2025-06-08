# Databricks notebook source
!pip install databricks_genai_inference==0.2.3
dbutils.library.restartPython()

# COMMAND ----------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from databricks_genai_inference import Embedding

embedding_response = Embedding.create(
    model="bge-large-en",
    input=["what is the exact value of pi?"]
)

df = pd.DataFrame(embedding_response.embeddings)

df.T

# Create a

# COMMAND ----------

### prompt Engineering ###
import numpy as np
import pandas as pd

system_prompt = "you are a pirate"
user_prompt = "what is the exact value of pi?"

chat_response = ChatCompletion.create(
    model="chat_completion",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    max_tokens=100
)
print(chat_response)

# COMMAND ----------

