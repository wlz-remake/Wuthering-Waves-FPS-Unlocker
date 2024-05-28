# 鸣潮帧率解锁器

本程序用于解锁游戏《鸣潮》的帧率上限，将其从 60 帧提高到 120 帧。

## 功能介绍

先手动选择鸣潮启动器文件，之后程序会自动定位游戏配置文件并（仅）修改游戏配置文件中的帧率上限。

## 原理

在启动器所在目录中的 `\Wuthering Waves Game\Client\Saved\LocalStorage` 路径下有一个 `LocalStorage.db` 数据库文件，其中 `LocalStorage` 表中的 `GameQualitySetting` 键对应的值是一个包含各种游戏设置的 JSON 字符串，字符串中的 `KeyCustomFrameRate` 值即为帧率上限。

## 打包方法

如果你想自行打包该程序，可以按照以下步骤操作：

1. **安装 PyInstaller**：

   首先，你需要安装 `PyInstaller`。在命令提示符中运行以下命令：

   ```bash
   pip install pyinstaller
   ```

2. **打包程序**：

   ```bash
   pyinstaller --onefile --windowed wuthering_waves_fps_unlocker.py
   ```

3. **获取可执行文件**：

   打包完成后，PyInstaller 会在目录中创建一个 dist 文件夹，里面包含了一个独立的 `wuthering_waves_fps_unlocker.exe` 文件。

## 注意事项

- 使用前可先备份 `LocalStorage.db` 文件，以防修改过程中出现意外情况。
- 本程序仅用于学习和研究目的，请勿用于商业用途。
- 如果遇到任何问题，请确保你已经正确选择了鸣潮启动器文件，并且游戏目录结构未被修改。
