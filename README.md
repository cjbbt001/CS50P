# Harvard CS50P — Introduction to Programming with Python (2022)

- 课程主页：<https://cs50.harvard.edu/python>
- 课堂代码：<https://cdn.cs50.net/python/2022/x/lectures/>

## 作业目录

### Week0 函数与变量

- `indoor.py` — 输入转小写
- `playback.py` — 空格替换为 `...`
- `einstein.py` — 按 E=mc² 计算能量
- `faces.py` — `:)` `:(` 转成表情符号
- `tip.py` — 解析 `$50.00` 与 `15%`，计算小费

### Week1 条件判断

- `deep.py` — 判断「终极答案」的几种写法
- `bank.py` — 按问候语返回 `$0` / `$20` / `$100`
- `extensions.py` — 文件扩展名转 MIME 类型
- `interpreter.py` — 解析 `x y z` 形式算术表达式
- `meal.py` — 按时间判断早餐 / 午餐 / 晚餐

### Week2 循环

- `camel.py` — camelCase 转 snake_case
- `coke.py` — 投币机，计算应付与找零
- `twttr.py` — 删除所有元音
- `plates.py` — 车牌校验
- `nutrition.py` — 查表输出水果热量

### Week3 异常

- `fuel.py` — 油量分数，输出 `E` / `F` / 百分比
- `taqueria.py` — 点单，累加总价
- `grocery.py` — 购物清单计数并按字母排序
- `outdated.py` — 日期格式统一为 `YYYY-MM-DD`

### Week4 库

- `game.py` — 猜数字
- `professor.py` — 十道算术题与计分
- `bitcoin.py` — 命令行参数校验 + 调 API 换算比特币价格
- `figlet.py` — ASCII 艺术字，支持 `-f` / `--font` 指定字体
- `emojize.py` — emoji 别名转换
- `adieu.py` — 用 `inflect` 拼出英语列举

### Week5 单元测试

pytest、`assert`。每个目录是「原模块 + `test_*.py`」，逻辑函数与 `main()` 分离以便 import。

- `test_twttr/` — 测试去元音
- `test_bank/` — 测试问候语换金额
- `test_plates/` — 测试车牌校验
- `test_fuel/` — 测试油量换算（含异常路径）

运行示例：

```bash
cd Week5/test_bank
pytest test_bank.py
```

### Week6 文件 I/O

- `lines/` — 统计 `.py` 文件有效代码行数
- `pizza/` — 用 `tabulate` 打印 CSV 菜单
- `scourgify/` — `before.csv` 清洗为 `after.csv`
- `shirt/` — 把衬衫图叠加到照片上

### Week7 正则表达式

- `numb3rs/` — 校验 IPv4（含测试）
- `um/` — 统计独立单词 `um` / `umm`（含测试）
- `response.py` — 校验邮箱格式
- `working/` — 12 小时制转 24 小时制（含测试）
- `watch/` — 从 HTML 中提取 YouTube 链接

### Week8 面向对象

- `jar/` — `Jar` 类实现 Cookie 罐存取（含测试）
- `seasons/` — 生日到今天的分钟数，转英文单词（含测试）
- `shritificate/` — 用 `fpdf2` 生成 CS50 衬衫证书 PDF

### Week9 Final Project

- `project.py` — 项目主程序，至少 3 个函数 + `main()`
- `test_project.py` — 对其中至少 3 个函数做 pytest 测试

## 环境

### 依赖库

第三方包（按需安装）：

| 包 | 用途 | 用于 |
| --- | --- | --- |
| `requests` | 调用 HTTP API | Week4/bitcoin |
| `pyfiglet` | ASCII 艺术字 | Week4/figlet |
| `inflect` | 英文单复数与列举 | Week4/adieu、Week8/seasons |
| `emoji` | emoji 别名转换 | Week4/emojize |
| `tabulate` | 表格输出 | Week6/pizza |
| `pillow` | 图像处理 | Week6/shirt |
| `fpdf2` | 生成 PDF | Week8/shritificate |
| `validators` | 邮箱格式校验 | Week7/response |
| `pytest` | 单元测试 | Week5、Week7、Week8、Week9 |

其余如 `sys`、`random`、`csv`、`re`、`datetime` 均为标准库。

```bash
pip install requests pyfiglet inflect emoji tabulate pillow fpdf2 validators pytest
```
