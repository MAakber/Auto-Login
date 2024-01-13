# 校园网自动登录工具

## 简介

学校校园网每天都要登录，自己懒得点了，于是就有了它
通过Edge开发工具实现自动登录校园网

## 功能

- 模拟用户登录校园网（在浏览器自动保存了的情况下只需要按登录就行）
- 通过外部文件修改配置文件，不需要Python环境

## 使用方法

### 使用现成的（推荐）

- 懒人模式 直接运行exe文件即可
- 根据提示进行操作

### 自己编译（也不是不行）

#### 依赖环境

- Windows 10及以上（Win7没试过）
- Python 3.10.11

#### 安装步骤

1. 克隆或下载本项目至本地。
2. 打开终端或命令提示符，进入项目目录。
3. 创建并激活Python虚拟环境（可选，但推荐）。
4. 运行`pip install -r requirements.txt`安装依赖。

#### 配置说明

在`setting.fcg`配置文件中设置以下参数：

- 登录URL（url，如果是网页认证）
- 按钮的元素ID（check_button）
- edge浏览器的版本号（ver)

**注意：** 不要改版本（ver）的参数 会坏掉的（悲）

#### 运行方式

在“启动”里面创建个文件快捷方式就好啦 这样电脑开机就会自动运行了

>在 Windows 10 中添加在启动时自动运行的应用

>选择“ 开始 ”按钮 ，然后滚动查找你希望在启动时运行的应用。

>右键单击该应用，选择 “更多” ，然后选择 “打开文件位置” 。 此操作会打开保存应用快捷方式的位置。 如果没有“ 打开文件位置 ”选项，这意味着该应用无法在启动时运行。

>文件位置打开后，按 Windows 徽标键 + R ，键入“ shell:startup ”，然后选择“ 确定 ”。 这将打开“ 启动 ”文件夹。

>将该应用的快捷方式从文件位置复制并粘贴到 “启动” 文件夹中。

## 注意事项

- 只能适用于浏览器保存了用户信息的情况！
- 本工具不会保存任何用户信息！只是模拟了用户登录的动作！
- Edge浏览器必须全部关闭 否则会报错