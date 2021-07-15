# Emoji-Prediction

![image](https://user-images.githubusercontent.com/41102775/61476404-9d4b4100-a9aa-11e9-81f4-77308961949a.png)

**Emojis** are small low resolution images used to express yourself better while writing a text.This project frees us from the cumbersome task of choosing the right emoji. In this project, the model predicts emojis according to a given sentence using Deep Learning Models.

# Input
Text data consiting of different sentences along with the labels. Labels represent a particular emoji representing the sentence. 

- **test_emoji.csv** -  for testing our model
- **train_emoji.csv** - for training our model


# Algorithm's Used
-RNN<br>
-LSTM

**Emoji Prediction.ipynb**   
This python script contains the code for both the models and their predictions.

# Result
**LSTM worked better than RNN** i.e. accuracy of the model is more by using LSTM than RNN.  
When we move from RNN to LSTM, we are introducing more & more controlling knobs, which control the flow and mixing of Inputs as per trained Weights. And thus, bringing in more flexibility in controlling the outputs.
So, LSTM gives us the most Control-ability and thus, Better Results. 
But also comes with more Complexity and Operating Cost.

# Additional Files
In this project, I have used the 6B 50D glove vector to build embedding matrix of words available in the glove vector.<br>
Download the 6B.50.50d.txt file and extract the file in the same directory as that of the code.<br>
Downloading Link-> [glove.6B.50D.txt](https://www.kaggle.com/watts2/glove6b50dtxt)

