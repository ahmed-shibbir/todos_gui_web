
# Importing modules and custom made functions
import streamlit as st
import functions



st.set_page_config(layout="wide")

st.title("My To Do App")
st.subheader("This is my to do app.")
st.write("<h1>This app is to regularly update <b>daily todos list</b>.</h1>",
         unsafe_allow_html=True)


# Populating todos list from the existing todos items
todos = functions.get_todos()


# Function to add an item to the todos list
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# st.checkbox("Orange")
# st.checkbox("Cherry")

# Adding an item to the todos list
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# Creasing checkbox list with items in the todos list
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # Removing an item from the todos list
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



# Session state display for convenience of coding(to be removed later)
# st.session_state