mkdir -p ~/.streamlit/
echo "[theme]
base="light"
primaryColor="#751a55"
secondaryBackgroundColor="#fbcfd5"
\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
