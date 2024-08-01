# streamlit-artifact
anthropic artifact implemented by streamlit

## Sample Input
python 3.12

```
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
```

```
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.bar_chart(chart_data)
```