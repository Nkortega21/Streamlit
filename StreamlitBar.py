import streamlit as st
import numpy as np
import pandas as pd
df = pd.DataFrame({
 'pets': ['dogs', 'cats', 'rabbits', 'birds'],
 'number': [42, 40, 3, 5],
 'family': ['canidae','felidae','leporidae','anatidae']
})
st.bar_chart(df, x="pets", y="number")#, color="family")