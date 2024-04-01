import streamlit as st
import plotly.graph_objects as go

# Assume your Sankey diagram functions are defined here
# Define the Sankey diagram functions
def create_sankey_human():
    fig = go.Figure(data=[go.Sankey(
      node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["Cooperate", "Defect", "Cooperate", "Defect"],
        color = ["green", "red", "green", "red"]
      ),
      link = dict(
        source = [0, 0, 1, 1], # (push, push, pull, pull)
        target = [2, 3, 2, 3], # (push, pull, push, pull)
        value = [3821, 7686, 3635, 10584] # human
    ))])

    fig.update_layout(title_text='Human', font_size=24)
    return fig

def create_sankey_gpt3():
    fig = go.Figure(data=[go.Sankey(
      node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["Cooperate", "Defect", "Cooperate", "Defect"],
        color = ["green", "red", "green", "red"]
      ),
      link = dict(
        source = [0, 0, 1, 1], 
        target = [2, 3, 2, 3], 
        value = [7, 15, 4, 4] # gpt-3
    ))])

    fig.update_layout(title_text='GPT-3', font_size=24)
    return fig

def create_sankey_gpt4():
    fig = go.Figure(data=[go.Sankey(
      node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["Cooperate", "Defect", "Cooperate", "Defect"],
        color = ["green", "red", "green", "red"]
      ),
      link = dict(
        source = [0, 0, 1, 1], 
        target = [2, 3, 2, 3], 
        value = [0, 26, 1, 3] # gpt-4
    ))])

    fig.update_layout(title_text='GPT-4', font_size=24)
    return fig

def create_sankey_gpt4_five():
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            label = ["Cooperate", "Defect", "", "", "", "", "", "", "Cooperate", "Defect"],
            color = ["green", "red", "green", "red", "green", "red", "green", "red", "green", "red"],
        ),
        link = dict(
            source = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
            target = [2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9],
            value = [0, 29, 1, 0, 0, 1, 25, 4, 17, 8, 4, 1, 17, 4, 8, 1] 
    ))])

    fig.update_layout(
    title_text='GPT-4',
    font_size=14,
    annotations=[
        dict(x=0, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Round 1"),
        dict(x=0.14, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Defect", font=dict(size=12, color='grey')),
        dict(x=0.25, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="2"),
        dict(x=0.38, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Defect", font=dict(size=12, color='grey')),
        dict(x=0.5, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="3"),
        dict(x=0.62, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Cooperate", font=dict(size=12, color='grey')),
        dict(x=0.755, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="4"),
        dict(x=0.93, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Cooperate", font=dict(size=12, color='grey')),
        dict(x=1, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="5")
    ],
)
    return fig

def create_sankey_gpt3_five():
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = ["Cooperate", "Defect", "", "", "", "", "", "", "Cooperate", "Defect"],
            color = ["green", "red", "green", "red", "green", "red", "green", "red", "green", "red"],
        ),
        link = dict(
            source = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
            target = [2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9],
            value = [6, 15, 1, 8, 5, 2, 9, 14, 10, 4, 5, 11, 12, 3, 2, 13]
    ))])
    
    fig.update_layout(
    title_text='GPT-3',
    font_size=14,
    annotations=[
        dict(x=0, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Round 1"),
        dict(x=0.14, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Defect", font=dict(size=12, color='grey')),
        dict(x=0.25, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="2"),
        dict(x=0.38, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Defect", font=dict(size=12, color='grey')),
        dict(x=0.5, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="3"),
        dict(x=0.62, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Cooperate", font=dict(size=12, color='grey')),
        dict(x=0.755, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="4"),
        dict(x=0.93, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="Cooperate", font=dict(size=12, color='grey')),
        dict(x=1, y=-0.2, xref='paper', yref='paper', showarrow=False, 
             text="5")
    ],
)
    return fig
# Title for the app
st.title('Sankey Diagrams')

# Sidebar dropdown for Human/GPT-3/GPT-4 graph selection
sankey_choice_human = st.sidebar.selectbox(
    'Select Sankey Diagram:',
    ('Human', 'GPT-3', 'GPT-4'),
    key='sankey_human'
)

# Function to display the selected Sankey diagram for Human/GPT-3/GPT-4
def display_sankey_human(choice):
    if choice == 'Human':
        fig = create_sankey_human()
    elif choice == 'GPT-3':
        fig = create_sankey_gpt3()
    else:  # GPT-4
        fig = create_sankey_gpt4()
    st.plotly_chart(fig, use_container_width=True)

# Sidebar dropdown for GPT-3/GPT-4 five rounds graph selection
sankey_choice_gpt = st.sidebar.selectbox(
    'Select Sankey Diagram (5 Rounds):',
    ('GPT-3', 'GPT-4'),
    key='sankey_gpt'
)

# Function to display the selected Sankey diagram for GPT-3/GPT-4 (5 Rounds)
def display_sankey_gpt(choice):
    if choice == 'GPT-4':
        fig = create_sankey_gpt4_five()
    else:  # GPT-3
        fig = create_sankey_gpt3_five()
    st.plotly_chart(fig, use_container_width=True)

# Display the selected Sankey diagrams
display_sankey_human(sankey_choice_human)
display_sankey_gpt(sankey_choice_gpt)
