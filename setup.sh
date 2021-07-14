mkdir -p ~/.streamlit/

echo "
[server]
headless = true
port = $PORT
enableCORS = false
[theme]
primaryColor = ‘#751A55’
backgroundColor = ‘#FFFFFF’
secondaryBackgroundColor = ‘#FBCFD5’
textColor= ‘#262730’
font = ‘sans-serif’
" > ~/.streamlit/config.toml
