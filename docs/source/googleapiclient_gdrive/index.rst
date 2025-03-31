GoogleAPIClient Google Drive Overview
==============================================================================


Overview
------------------------------------------------------------------------------
本文档记录了我如何使用 Google Drive API 来读写 Google Drive 内的文件.



1. 创建 Google Project
------------------------------------------------------------------------------
- 首先到 Google Cloud Console 的主界面.
- 然后创建一个 Project. Google Cloud 的设计哲学就是 Project 是一个用于隔离资源的容器, 你可以理解为一个 Namespace.
- 为这个项目创建的 Project 叫 `sh-google-drive-api-poc Google Project <https://console.cloud.google.com/welcome?inv=1&invt=AbrbNg&project=infinite-loader-453021-g5>`_


2. 创建 Client Secrets
------------------------------------------------------------------------------
如果你只是想写一个程序, 操纵你自己 Google Drive 账号里的文件 (例如上传, 下载, 删除, 修改等), 那么 Google Drive API 是最合适的, 而你在 Google Cloud 上创建 API 的方式, 建议使用 OAuth 2.0 方式的 "个人客户端" 凭证, 这样你的程序可以在你授权的情况下访问你的 Google Drive.

下面是创建 OAuth 要用到的 Client Secrets 的详细步骤:

- 首先进入 `Google Auth Platform <https://console.cloud.google.com/auth/overview?inv=1&invt=AbrbWA&project=infinite-loader-453021-g5>`_ 产品界面.
- 你在左边会看到 ``Branding``, ``Audience``, ``Clients`` 等, 其中 Clients 就是我们需要的界面.
- 进入 Clients 界面后, 点击 Create Client 按钮, Application Type 选择 Desktop (也就是在你个人电脑上用的那种 App), 然后给它一个名字, 比如我的叫做 ``gdrive-pathlib-dev-laptop``, 然后点击 Create 按钮. 之后你需要点击下载按钮将这个 Client Credentials 下载下来, 保存到一个安全的地方. 这是你唯一一次能看到这个 Credentials 的机会, 如果这次不下载, 下次就看不到了, 只能删掉重建.

这里详细讲解一下 Credentials.json 文件. 在现代的云计算 API 设计中, 一般最终的鉴权信息都是定时过期的. 就拿我比较熟悉的 AWS 为例, 你的 AWS ACCESS KEY 和 SECRET KEY 就像一对 username, password 一样, 每次用 API 之前首先验证身份 (告诉云计算服务器你是谁), 然后服务器根据你的 Permission Scope 给你一个 Token, 你再拿着 ACCESS KEY, SECRET KEY, TOKEN 三个一起去调 API. 这个 TOKEN 自带刷新机制, 一段时间过期后, 如果你访问的来源比如 IP 地址等信息能证明你是之前使用过这个 TOKEN 的人 (或机器), 只不过 TOKEN 过期了, 服务器会自动给发一个新 TOKEN, 然后客户端程序会自动使用这个新 TOKEN 的.

而这里的 Credentials.json 就是这个 ACCESS KEY, SECRET KEY (google 叫 Client Secret). 你后面用官方文档中的示例脚本做实验的时候, 第一次运行程序就会弹出一个浏览器窗口, 要求你登录 Google Account 鉴权, 然后才会给你这个 TOKEN, 然后官方文档中的示例脚本就有一段代码将其保存到本地, 以后就不用谈浏览器窗口了, 就会自动走自动刷新 TOKEN 的流程.


3. OAUTH consent Screen
------------------------------------------------------------------------------
你平时使用第三方插件时, 比如手机拍照上传到 Google Drive 的程序, 肯定会看到弹出一个窗口说这个程序服务来自于某某公司, 你是否要允许这个程序访问你的 Google Drive. 这个窗口就是 OAuth Consent Screen. 虽然这个 App 是你自己创建的, 但你也要有这个程序. 你需要到 `Google Auth Platform -> Branding <https://console.cloud.google.com/auth/branding?project=infinite-loader-453021-g5>`_ 页面, 填写下列信息:

- Application home page: 公开可见的你的 App 官网, 我填的是 https://github.com/MacHu-GWU/learn_pylib-project/tree/main/docs/source/googleapiclient_gdrive
- Application privacy policy link: 你的隐私协议链接, 我填的是 https://github.com/MacHu-GWU/learn_pylib-project/tree/main/docs/source/googleapiclient_gdrive/terms-of-service-link
- Application terms of service link: 你的用户协议链接, 我填的是 https://github.com/MacHu-GWU/learn_pylib-project/tree/main/docs/source/googleapiclient_gdrive/privacy-policy-link
- Developer contact information: 我填的自己的 Email.

简单来说 Google 要求你就是把自己的信息注册了, 你的 App 才能用.


4. 把自己添加为 Test User
------------------------------------------------------------------------------
Google 现在对 OAuth 2.0 访问其服务（如 Gmail、Google Drive）有更严格的安全要求:

- 如果你创建了一个新的 OAuth 客户端 ID, 它默认处于 "测试模式".
- 处于测试模式的应用, 只能由开发者添加的测试用户使用, 其他人无法使用.

你需要将你自己的 Google 账号添加到测试用户列表中, 不然在上面提到的弹出浏览器窗口验证的时候就会看到你的 App 被禁止访问的提示.

具体做法是:

- 到 `Google Auth Platform -> Audience <https://console.cloud.google.com/auth/audience?inv=1&invt=Abrbag&project=infinite-loader-453021-g5>`_ 页面中找到 TEST USER, 并添加自己的 Google Account 的 Email 既可.


References
------------------------------------------------------------------------------
- `Google Drive API - Python Quick Start <https://developers.google.com/drive/api/quickstart/python>`_:
