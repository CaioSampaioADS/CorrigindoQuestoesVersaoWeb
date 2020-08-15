mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"caio.h.sampaio@outlook.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml