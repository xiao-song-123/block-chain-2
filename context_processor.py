from c5_database import User
from flask import Flask

app = Flask(__name__)


# 模板上下文处理函数
@app.context_processor
def inject_user():  # 函数名可以随意修改
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于return {'user': user}
# 这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中
# 因此可以直接在模板中使用。
