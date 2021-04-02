## Startup 

文本编辑器：Visual Studio Code。
C/C++编译器：gcc/g++(Linux)、clang(macOS)、msvc(Windows)。
C/C++调试器：gdb(Linux)、lldb(macOS)、msvc(Windows)。
构建工具：CMake、Make。

### CMake

1. Download [CMake](https://cmake.org/download/)
2. add Environment Path. Copy Cmake.app Menu `Tools - How to Install For Command Line Use - install symlinks`
3. VSCode install extension `CMake` and `CMake Tools`
4. Create one dir and use Command(`cmd + shift + p`/`f1`), `CMake: Quick Start`
5. use Command, `CMake: Configure`
6. use Command, `CMake: Clean Rebuild`

### Debug



```js
// .vscode/launch.json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "type": "lldb",
      "request": "launch",
      "name": "Debug",
      "program": "${workspaceFolder}/build/cmake_cpp_boilerplate",
      "args": [],
      "cwd": "${workspaceFolder}"
    }
  ]
}
```