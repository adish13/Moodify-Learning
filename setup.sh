mkdir -p ~/.streamlit/

echo "\
[theme]\n\
primaryColor = "#E694FF"\n\
backgroundColor = "#00172B"\n\
secondaryBackgroundColor = "#0083B8"\n\
textColor = "#DCDCDC"\n\
font = "sans-serif"\n\
" > ~/.streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
