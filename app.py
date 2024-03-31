import streamlit as st
import plotly.graph_objects as go

# Define the two Sankey diagrams as functions for clarity
def create_sankey_gpt4():
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            label=["Cooperate", "Defect", "", "", "", "", "", "", "Cooperate", "Defect"],
            color=["green", "red", "green", "red", "green", "red", "green", "red", "green", "red"],
        ),
        link=dict(
            source=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
            target=[2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9],
            value=[0, 29, 1, 0, 0, 1, 25, 4, 17, 8, 4, 1, 17, 4, 8, 1]
    ))])

    fig.update_layout(title_text='GPT-4', font_size=14)
    return fig

def create_sankey_gpt3():
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=["Cooperate", "Defect", "", "", "", "", "", "", "Cooperate", "Defect"],
            color=["green", "red", "green", "red", "green", "red", "green", "red", "green", "red"],
        ),
        link=dict(
            source=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
            target=[2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9],
            value=[6, 15, 1, 8, 5, 2, 9, 14, 10, 4, 5, 11, 12, 3, 2, 13]
    ))])
    
    fig.update_layout(title_text='GPT-3', font_size=14)
    return fig

# Streamlit UI
st.title('Sankey Diagram Comparison: GPT-4 vs. GPT-3')

# Dropdown for graph selection
option = st.selectbox(
    'Choose a model to view its Sankey diagram:',
    ('GPT-4', 'GPT-3')
)

# Display the chosen graph
if option == 'GPT-4':
    st.plotly_chart(create_sankey_gpt4())
else:
    st.plotly_chart(create_sankey_gpt3())

# Link to related article
st.markdown('Read the related article [here](https://www.pnas.org/doi/10.1073/pnas.2313925121).')
