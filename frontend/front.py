import streamlit as st
import requests
import json
import time


def create_todo():
    st.title('新規登録')
    with st.form(key='新規登録'):
        deadline = st.date_input('期日').strftime('%Y-%m-%d')
        todo = st.text_input('Todo', max_chars=100)
        priority = st.number_input(
            label='優先度', min_value=0, max_value=10, value=0)
        genre = st.text_input('カテゴリ', max_chars=15)
        submit_button = st.form_submit_button(label='登録')

        if submit_button:
            data = {
                'deadline': deadline,
                'todo': todo,
                'priority': priority,
                'genre': genre
            }
            response = post_data(data)
            print(response, type(response))
            handle_response(response, '登録')

            time.sleep(1)
            st.rerun()


def fetch_todos():
    url = 'http://127.0.0.1:8000/todos'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError as e:
            st.error(f'JSONデコードエラー: {e}')
            st.error(f'レスポンステキスト: {response.text}')
            return None
    else:
        st.error(f'エラーが発生しました: {response.status_code}')
        st.error(f'レスポンステキスト: {response.text}')
        return None


def post_data(data):
    url = 'http://127.0.0.1:8000/todos'
    response = requests.post(url, json=data)
    return response


def patch_data(data, todo_id):
    url = f'http://127.0.0.1:8000/todos/{todo_id}'
    response = requests.patch(url, json=data)
    return response


def delete_todo(todo_id):
    url = f'http://127.0.0.1:8000/todos/{todo_id}'
    response = requests.delete(url)
    return response


def handle_response(response, action):
    if response.status_code == 200:
        st.success(f'{action}成功')
    else:
        st.error(f'エラーが発生しました: {response.status_code}')
        st.error(response.text)


page = st.sidebar.selectbox('ページ名', ['新規登録', '未完了リスト', '完了リスト'])

if page == '新規登録':
    create_todo()

elif page == '未完了リスト':
    st.title('未完了リスト')
    records = fetch_todos()
    uncompleted_todos = [
        record for record in records if not record.get('is_done')]

    if not uncompleted_todos:
        st.write('未完了のTodoはありません')
    else:
        for i, record in enumerate(uncompleted_todos):
            todo_id = record.get('id')

            with st.form(key=str(i)):
                st.subheader('・'+record.get('deadline'))
                st.write(record.get('todo'))
                submit_button_1 = st.form_submit_button(label='完了')
                submit_button_2 = st.form_submit_button(label='削除')

                if submit_button_1:
                    data = {**record, 'is_done': True}
                    if todo_id is not None:
                        response = patch_data(
                            data, todo_id)
                        handle_response(response, '完了')
                    else:
                        st.error('エラー: Todo IDが見つかりません')

                if submit_button_2:
                    todo_id = record.get('id')
                    if todo_id is not None:
                        response = delete_todo(todo_id)
                        handle_response(response, '削除')
                    else:
                        st.error('エラー: Todo IDが見つかりません')

elif page == '完了リスト':
    st.title('完了リスト')
    records = fetch_todos()
    completed_todos = [record for record in records if record.get('is_done')]

    if not completed_todos:
        st.write('完了したTodoはありません')
    else:
        for i, record in enumerate(completed_todos):
            st.subheader('・'+record.get('deadline'))
            st.write(record.get('todo'))
