# 🎻 ViolinBear – 小提琴自动指法识别与推荐 App

🌏 语言切换: [English](README.md) | [中文](README.zh.md)

## 📝 项目简介
**ViolinBear** 是一个专注于**小提琴乐谱图像自动识别与智能指法推荐**的开源项目。

通过结合光学乐谱识别（OMR）技术与小提琴演奏逻辑算法，本项目能够让小提琴初学者和爱好者通过手机/iPad 拍照或上传乐谱图片，瞬间在谱面上获得直观的琴弦与指法标注引导。

📺 **项目演示视频**:
- [YouTube Shorts 演示](https://www.youtube.com/shorts/TlUFP1Flaps)
- [小红书 演示](https://www.xiaohongshu.com/discovery/item/6880bcbc000000000d025b9f?source=webshare&xhsshare=pc_web&xsec_token=ABt0iDrK6-_G90slb4FPPuK52brwTRIXRSWnoTB8SuRXU=&xsec_source=pc_share)

---

## 🏗 技术架构
本项目采用前、后端解耦的架构设计：

- **前端 (Swift + SwiftUI)**: 原生 iOS/iPadOS 应用。负责调用相机/相册上传乐谱、高保真乐谱画布渲染，以及动态指法圆点交互。
- **后端 (Flask)**: 轻量级 Python 后端服务。负责调度本地 OMR 引擎、数据处理并提供 API 接口。
- **OMR 引擎 (Java / Audiveris)**: 纯本地运行的 `audiveris.jar` 核心组件。负责将乐谱图片转译为标准的数字化格式（`MusicXML`）。
- **核心中间件 (Python Algorithm)**: 本项目的“大脑”。解析 XML 结构，并根据小提琴物理手位计算最优指法路径。

---

## 🛠 环境配置与本地启动

请按照以下步骤配置本地 Mac 开发环境，将前后端完整运行起来。

### 前置准备
- **Python 3.10+**
- **Java JDK 17+** (用于在本地后台执行 `audiveris.jar`)
- **Xcode** (包含 iOS/iPadOS 17+ SDK，用于编译前端应用)

---

### 1. 后端配置与启动 (Python + OMR)

#### 步骤 1: 进入后端工作目录
```bash
cd violin_backend
```

#### 步骤 2: 安装 Python 依赖
为避免系统环境冲突，建议直接使用以下命令安装核心框架：
```bash
/usr/bin/python3 -m pip install flask flask-cors requests
```

#### 步骤 3: 验证 Java 运行环境
确保终端能顺利调用 Java 虚拟机：
```bash
java -version
```
*(如报错请前往 Oracle 官网或 adoptium.net 安装标准 macOS JDK)。*

#### 步骤 4: 启动 Flask 服务
```bash
/usr/bin/python3 app.py
```
看到以下日志即代表启动成功（请保持此终端窗口运行）：
```text
* Serving Flask app 'app'
* Debug mode: on
* Running on all addresses (0.0.0.0)
* Running on [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Running on [http://172.28.96.34:8000](http://172.28.96.34:8000) (你的局域网本地 IP)
```

---

### 2. 前端配置与真机运行 (iOS / iPadOS)

#### 步骤 1: 使用 Xcode 打开项目
在 Finder 中进入 `Frontend/ViolinBear` 文件夹，双击 **`ViolinBear.xcodeproj`** 打开完整项目。

#### 步骤 2: 修改后端 API 地址
在 Xcode 中使用 `Cmd + Shift + F` 搜索 API 地址变量（如 `baseURL`）：
- **iPad/iPhone 真机调试（推荐）**：改为 Mac 终端显示的局域网 IP（如 `http://172.28.96.34:8000`），确保 Mac 与 iOS 设备在同一 Wi-Fi 下。
- **模拟器调试**：保持 `http://127.0.0.1:8000`。

#### 步骤 3: 开发者签名与权限
1. 在 **Signing & Capabilities** 面板的 **Team** 中选择你的 Apple ID。
2. 若使用真机，需在 iOS 设备的 *设置 -> 隐私与安全* 中开启 **开发者模式 (Developer Mode)**。

#### 步骤 4: 编译运行
在 Xcode 顶部选择你的设备，按下 **`Cmd + R`**（或点击 🔼 运行按钮）将 App 安装到设备。

---

## 🗺 阶段路线图

### 阶段一：基础逻辑验证 (MVP - 当前版本)
- [x] 纯本地 Python 后端 + Java OMR 调度链路。
- [x] 硬编码第一把位（1st Position）指法映射模型（D4–A4 音域边界）。
- [x] 解析 MusicXML 并输出结构化 JSON 坐标及指法标签。
- [x] SwiftUI 画布高精度指法圆点动态渲染。

### 阶段二：多把位与启发式换把 (下一步计划)
- [ ] 扩展指法矩阵模型（支持第 3、第 5 及更高把位）。
- [ ] 引入启发式图搜索算法，实现“换把摩擦最小化”和“避免冗余跨弦”的最优路线规划。
- [ ] 优化复杂切分音及临时升降号（Accidentals）的支持。

### 第三阶段：边缘端侧 AI 推理 (远期展望)
- [ ] 基于 Swift 原生 CoreML 架构，将 OMR 识别完全下沉至本地设备（完全离线）。
- [ ] 结合 Suzuki 及 IMSLP 乐谱集，训练生成式指法模型，支持不同流派的风格化推荐。

---

## 🤝 欢迎贡献
本项目仍处于早期孵化阶段，代码迭代迅速。非常欢迎开发者、算法专家和音乐爱好者参与：

- **遇到问题？** 提交 Issue，附上报错日志或原谱截图。
- **有算法优化建议？** 欢迎直接重构 Python 中间件逻辑并提交 PR！
- **使用体验反馈：** 我们非常期待听到 ViolinBear 在处理你的日常曲谱时的表现。

让我们一起把 ViolinBear 打造成对全球小提琴社区真正有价值的开源利器！ 🎻
