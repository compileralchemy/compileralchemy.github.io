title: Laith: Native Android Apps In Pure Python
---
Started a project over the week end called laith: Writing native Android apps using pure Python. It is still ongoing.

To be as efficient as possible, you need to get close to how Android works. This project takes the hard route: Compiling Python to Kotlin and C++. There are some caveats to this approach, of course. Like not using the full power of Python like changing attributes dynamically etc. But, this constrasts with other Python approaches where you have to bundle an interpreter with your Android app.

This has a nice base already where you can call APIs dynamically so that if tomorrow we don't support a feature that Google released, you can still access it. It is powerful and serves it's purpose, but, still unstable.

Dx-wise, i choose React Native as i like it's approach better than even developing directly in Android Studio.

```
$ laith init app
$ cd app
$ laith run 
```

'laith run' runs in the configured adb emulator or device. Contributions welcome!
