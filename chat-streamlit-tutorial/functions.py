import os

import streamlit as st
from dotenv import load_dotenv


def get_secret(key, default=None):
    """Read a secret from Streamlit secrets or the local environment."""
    try:
        return st.secrets[key]
    except Exception:
        load_dotenv()
        return os.getenv(key, default)
