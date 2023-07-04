## Frequently Asked Questions

Check the `README.md` for instructions on how to compile the program. The   `README.md` also has a detailed command list (that you can also see with `-h` flag) and a list of some useful features.
Here are some additional Questions and Answers from previously submitted [issues](https://github.com/kuvaus/LlamaGPTJ-chat/issues). I hope these are of help. Thanks for everyone who submitted an issue or commented on them.

### Q: I get the illegal instruction error. [#21](https://github.com/kuvaus/LlamaGPTJ-chat/issues/21)
A: If you're getting an illegal instruction error, it could be because your processor doesn't understand the AVX2 instructions. In that case, try using the `chat-windows-latest-avx.exe` instead of `chat-windows-latest-avx2.exe`. If the error still occurs, you can try adding the `-DAVX2=OFF` flag in the cmake when you compile the program. This flag disables the AVX2 instructions. Here's an example of how to compile with the flag:
```
mkdir build
cd build
cmake .. -DAVX2=OFF
cmake --build . --parallel
```

### Q: How can I generate longer answers? [#17](https://github.com/kuvaus/LlamaGPTJ-chat/issues/17)
A: To generate longer answers, you can set the `n_predict` parameter to a larger number. By default, it is set to 200. You can also try prompting the AI with phrases like "tell me more" to encourage it to expand the answer. Make sure to mention in the prompt that you want a long answer. Here's an example of how to set the `n_predict` parameter:
```
./chat-program --model "your model" --n_predict 500
```

### Q: Is there any way to produce deterministic results? [#14](https://github.com/kuvaus/LlamaGPTJ-chat/issues/14)
A: Yes, you can produce deterministic results by using the `--top_k 1` flag. This restricts the model to choose the most likely result. Alternatively, you can set the temperature to a very low number, such as `--temp 0.001`. Both of these options will make the model more deterministic. Here's an example of how to use these flags:
```
./chat-program --model "your model" --top_k 1
```
or
```
./chat-program --model "your model" --temp 0.001
```

### Q: Is there any way to reset the chat? [#10](https://github.com/kuvaus/LlamaGPTJ-chat/issues/10)
A: Yes, you can reset the chat by using the `/reset` command. Simply type `/reset` in the chat and it will reset the chat context. This can be useful if you want to start a new conversation or clear the current context.

### Q: I get llama errors when compiling [#9](https://github.com/kuvaus/LlamaGPTJ-chat/issues/9)
A: If you're getting llama errors when compiling, make sure you added the `--recurse-submodules` flag when cloning the git repository. Without this flag, it won't load the `llama.cpp` into the backend folder. Here's an example of how to clone the repository with the flag:
```
git clone --recurse-submodules https://github.com/kuvaus/LlamaGPTJ-chat
```
If you have already cloned the repository without the flag, you can try running the following command to download the `llama.cpp`:
```
git submodule update --remote
```

### Q: How can I add a context? For example, I would like to create a chatbot which would ask me to select between 3 products. [#8](https://github.com/kuvaus/LlamaGPTJ-chat/issues/8)
A: To add a context, you can create a "prompt template" text file. In the template file, you can define the instructions, prompt, and response format. Then, when you load the program, you can specify the template file using the `--load_template` flag. Here's an example of how to create a prompt template file and load it:
```
"promptTemplate.txt"
```
```
### Instruction:
You are managing a fruit shop that sells three items: apples, strawberries, and oranges. Listen to what the user requests and respond accordingly.
### Prompt:
%1
### Response:
```
```
./chat-program --model "your model" --load_template "./promptTemplate.txt"
```

### Q: Which model do you recommend? [#8](https://github.com/kuvaus/LlamaGPTJ-chat/issues/8)
A: The recommended model depends on your use-case. Models with more parameters will generally perform better, but they are also larger in size and take longer to generate answers. You can find a list of available models [here](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-chat#manual-download-of-models). As a base, the `ggml-gpt4all-j-v1.3-groovy` model should work fine
