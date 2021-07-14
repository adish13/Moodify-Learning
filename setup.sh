mkdir -p ~/.streamlit/
echo "\
[theme]\n\
base="light"\n\
primaryColor="#751a55"\n\
secondaryBackgroundColor="#fbcfd5"\n\
\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
