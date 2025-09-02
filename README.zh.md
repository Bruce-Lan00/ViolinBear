# 🎻 ViolinBear – 小提琴自动指法 App

🌏 语言: [English](README.md) | [中文](README.zh.md)

## 项目简介
ViolinBear 是一个 **小提琴谱自动识别与指法推荐** 的开源项目。  
它结合 **[Audiveris OMR](https://github.com/Audiveris/audiveris)**、**Python 后端逻辑** 和 **SwiftUI 前端 App**，帮助学习者和演奏者快速得到乐谱的指法标注。  

请观看这个简单的**[演示视频](https://www.xiaohongshu.com/discovery/item/6880bcbc000000000d025b9f?source=webshare&xhsshare=pc_web&xsec_token=ABt0iDrK6-_G90slb4FPPuK52brwTRIXRSWnoTB8SuRXU=&xsec_source=pc_share)**：

---

## 架构设计
- **前端 (Swift + SwiftUI)**:  
  界面、笔记功能、上传谱图  
- **后端 (Flask / FastAPI)**:  
  调用 Audiveris，管理缓存与结果  
- **识谱引擎 (Docker + Java)**:  
  将谱图转换为 MusicXML/JSON  
- **中间层 (Python)**:  
  格式转换与指法逻辑封装  
- **数据库 (PostgreSQL / MongoDB)**:  
  储存谱图、用户资料、识别结果  

---

## 功能规划
### 阶段一：基础逻辑验证
- 硬编码第一把位音符表（D4–A4 等）  
- 解析 MusicXML，判断是否可用第一把位演奏  
- 返回包含弦号和指法的 JSON  

### 阶段二：多把位智能选择
- 维护多把位映射表 + 启发式规则（少换把位、避免跨弦）  
- 为整段旋律生成最优指法路线  

### 阶段三（可选）：机器学习
- 收集 Suzuki、IMSLP 等教材谱例  
- 训练模型，学会风格化推荐指法  

---

## Roadmap
- **MVP（现在）**: 后端识谱 + App 展示（必须联网）  
- **2.0**: JSON 缓存 + 离线展示（初次联网后可离线使用）  
- **3.0**: Swift 内嵌推理模型 → 完全离线运行  

---

## 🤝 欢迎贡献
本项目仍处于早期阶段，很多功能尚未完成。  
非常欢迎开发者和音乐爱好者一起来参与：  

- 提交 Issue（功能建议 / Bug 报告）  
- 提交 PR（代码、算法、UI 改进）  
- 分享想法与使用体验  

让我们一起把 ViolinBear 打造成真正有用的工具！
