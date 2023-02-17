import streamlit as st
import functions

todoList = functions.current_list()


# Create a function that adds a new to do item to the list when the user adds an item in the st.text_input function
# below
def add_todo():
    todo = st.session_state["new_todo_input"]
    todoList.append(f"\n{todo}")
    functions.write_to_list(todoList)
    # resetting the text input box to blank after a item is appended
    st.session_state["new_todo_input"] = ""


def complete(list, index_list):
    todolist_local = list
    for index_local in index_list:
        print(index_local)
        todolist_local.pop(index_local)
    functions.write_to_list(todoList)
    del st.session_state[f"{index}.{item}"]
    st.experimental_rerun()


# Creates the title of the page
st.title("Project Management App")
st.subheader("What needs to be done?")
st.text("Known issues:\n"
        "When adding the first item it creates an extra blank space.\n"
        "When completing more than one item it will keep the last task completed but then complete the one after the "
        "last selected task\n"
        "If you are entering a a number followed by \".\" it will return a blank value (Ex: 23.)")

list_of_index = []

for index, item in enumerate(todoList):
    checkbox = st.checkbox(item, key=f"{index}.{item}")
    if checkbox:
        item_index = index
        list_of_index.append(item_index)
print(list_of_index)

st.text("")
if st.button(label="Complete", key="Complete Button"):
    complete(todoList, list_of_index)

# Input box on the web page
st.text_input(label="", placeholder="Enter a new item..",
              on_change=add_todo, key="new_todo_input")

st.session_state
