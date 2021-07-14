mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = ‘#751A55’
backgroundColor = ‘#FFFFFF’
secondaryBackgroundColor = ‘#FBCFD5’
textColor= ‘#262730’
font = ‘sans-serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
