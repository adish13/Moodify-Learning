mkdir -p ~/.streamlit/

echo "[theme]
base="light"
primaryColor="#751a55"
secondaryBackgroundColor="#fbcfd5"
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
