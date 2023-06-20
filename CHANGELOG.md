
## Changelog

#### [Upcoming](https://github.com/kuvaus/workflowtest/compare/v0.2.9...HEAD)

#### [v0.2.9](https://github.com/kuvaus/LlamaGPTJ-chat/releases/tag/v0.2.9)

- Add this [changelog](https://github.com/kuvaus/LlamaGPTJ-chat/CHANGELOG.md) :)
- Add sha256 hashes on release so you can verify the binaries
- All binaries are automatically generated with Github actions
- Add signal handling for SIGHUP (macOS, Linux) and CTRL_CLOSE_EVENT (Windows) to fix issue [`#XXXX`](https://github.com/kuvaus/LlamaGPTJ-chat/issues/XXXX)
- This allows you to run chat as a subprocess. The chat subprocess now quits properly if parent app is closed.
- Better debug mode compilation. May fix issue [`#XXXX`](https://github.com/kuvaus/LlamaGPTJ-chat/issues/XXXX)

#### [v0.2.8](https://github.com/kuvaus/LlamaGPTJ-chat/releases/tag/v0.2.8)
> 16 June 2023

- Adds `--save_dir` option so you can change save directory location
- Default location is `./saves` on the same directory as the chat binary
- See issue [`#13`](https://github.com/kuvaus/LlamaGPTJ-chat/issues/13) for more details

#### [v0.2.7](https://github.com/kuvaus/LlamaGPTJ-chat/releases/tag/v0.2.7)
> 15 June 2023

- Fixes for old macOS.
- Use `-DOLD_MACOS=ON` option when compiling with CMake.
- Tested to compile on High Sierra and Xcode 10
