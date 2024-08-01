import streamlit as st
import pandas as pd
import numpy as np

# 设置页面标题
st.title("代码输入与执行")

# 用户输入
user_code = st.text_area("输入你的代码：", height=200)

# 显示代码
st.code(user_code, language="python")

# 执行代码并显示结果
if st.button("执行代码"):
    if user_code:
        try:
            # 定义一个局部命名空间来执行用户代码
            local_namespace = {}
            
            # 执行用户代码
            exec(user_code, {"st": st, "pd": pd, "np": np}, local_namespace)
            
            # 从局部命名空间中获取变量并显示
            for var_name, var_value in local_namespace.items():
                if isinstance(var_value, pd.DataFrame):
                    st.write(f"变量 `{var_name}` 的值为：")
                    st.dataframe(var_value)
                else:
                    st.write(f"变量 `{var_name}` 的值为：{var_value}")
        except Exception as e:
            st.error(f"代码执行出错：{e}")
    else:
        st.warning("请输入一些代码以执行。")