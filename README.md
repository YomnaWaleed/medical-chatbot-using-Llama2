# medical chatbot using Llama2

# How to run?
### STEPS:

Clone the repository

```bash
project repo: https://github.com/YomnaWaleed/medical-chatbot-using-Llama2.git
```

### STEP 01- Create a conda environment after opening the repostory 

```bash
conda create -n mchatbot python=3.8 -y
```

```bash 
conda activate mchatbot
```

### STEP 02- install the requirements 
```bash
pip install -r requirements.txt 
```

### Download the quantize model from link provided in model folder & keep the model in the model directory "

```ini
## Download the Llama 2 model :
llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following Link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the flollowin command
python app.py
```

Now, 
```bash 
open up localhost:
```

### Techstack Used:

- Python
- Langchain
- Flask 
- Meta Llama2
- Pinecone
