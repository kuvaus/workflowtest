## Frequently Asked Questions

Check the `README.md` for instructions on how to compile the program. The   `README.md` also has a detailed command list (that you can also see with `-h` flag) and a list of some useful features.
Here are some additional Questions and Answers from previously submitted [issues](https://github.com/kuvaus/LlamaGPTJ-chat/issues). I hope these are of help. Thanks for everyone who submitted an issue or commented on them.

### Q: I get the illegal instruction error. [#21](https://github.com/kuvaus/LlamaGPTJ-chat/issues/21)

**A:** Try the `chat-windows-latest-avx.exe` instead of `chat-windows-latest-avx2.exe`

I've had the illegal instruction error when a processor does not understand the avx2 instructions.

If the error still happens then I need to think about it more.

If you compiled it yourself, try adding the `-DAVX2=OFF` flag in the cmake:

```
mkdir build
cd build
cmake ..  -DAVX2=OFF
cmake --build . --parallel
```


### Q: How can I generate longer answers? [#17](https://github.com/kuvaus/LlamaGPTJ-chat/issues/17)

**A:** Set `n_predict` to a big number:
```
  -n N, --n_predict  N  number of tokens to predict (default: 200)
```
You can also say to the AI "tell me more" or something like that and it usually expands the answer. Maybe you also need to say in the prompt that you want a long answer.



### Q: Is there any way to produce deterministic results? [#14](https://github.com/kuvaus/LlamaGPTJ-chat/issues/14)

**A:** Use `--top_k 1` to restrict the model to choose the most likely result. Alternatively, you can set the temperature to a very low number `--temp 0.001`


### Q: Is there any way to reset the chat? [#10](https://github.com/kuvaus/LlamaGPTJ-chat/issues/10)

**A:** Use the `/reset` command

### Q: I get llama errors when compiling [#9](https://github.com/kuvaus/LlamaGPTJ-chat/issues/9)

**A:** First, did you add the `--recurse-submodules` when cloning the git? Without that it won't load the llama.cpp into the backend folder. Like this:
```
git clone --recurse-submodules https://github.com/kuvaus/LlamaGPTJ-chat
```
If you had already cloned the repo, this might also work (it should download the llama.cpp):
```
git submodule update --remote
```

### Q: How can I add a context? For example, I would like to create a chatbot which would ask me to select between 3 products. [#8](https://github.com/kuvaus/LlamaGPTJ-chat/issues/8)

    Apple
    Strawberry
    Orange.
    And then ask what product I want and how much. How do I create that context?

**A:**
To do this, you must first create a "prompt template" text file. Then, give the correct system message to the assistant, and then load the template when you load the program.

So something like this would work.

"promptTemplate.txt"
```
### Instruction:
You are managing a fruit shop that sells three items: apples, strawberries, and oranges. Listen to what the user requests and respond accordingly.
### Prompt:
%1
### Response:
```
Then, to load the template when you load the program:
```
./chat-program --model "your model" --load_template "./promptTemplate.txt"
```

### Q: Which model do you recommend? [#8](https://github.com/kuvaus/LlamaGPTJ-chat/issues/8)

**A:** This depends on the use-case. Models that have lots of parameters (B) will be better. However, those are always bigger in size and will take longer to generate the answers.

[You can click here](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-chat#manual-download-of-models) to see all the models you can use. As a base, you should be fine with [ggml-gpt4all-j-v1.3-groovy](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin)
