# *Table of Contents*
- [*Table of Contents*](#table-of-contents)
- [前置き](#前置き)
- [工夫点](#工夫点)
- [開発方針](#開発方針)
  - [フォルダ名と用途](#フォルダ名と用途)
  - [Backend folder structure](#backend-folder-structure)
- [Preface](#preface)
- [Noteworthy Points](#noteworthy-points)
- [Dev outline](#dev-outline)
  - [Folder name and usage](#folder-name-and-usage)
  - [Backend folder structure](#backend-folder-structure-1)

※ English follows Japanese.
# 前置き
- このアプリは[Zennの記事](https://zenn.dev/tirimen/articles/7b5861c40e8a77)をベースに作成しました
- [生成系AI](https://chat.openai.com/)を用いながらコーディングを進めました

# 工夫点
- その上で，，以下のような創意工夫を加えています
  - クエリの整合性
    - クエリ呼び出しの効率化と簡略化のためのデータベースモデル
    - IDベースのクエリ呼び出しによるデータ管理の一貫性
  - 可読性
    - 型定義によるエラーの軽減
    - 簡潔で読みやすいコード
    - アプリの説明，フォルダ構造，セットアップ，使用方法を含む具体的で論理的なReadMeファイル
  - プロセス
    - データの挿入，更新，削除に対するエラーハンドリング
    - デバッグの容易化のための処理切り分けと関数定義

# 開発方針
基本的なフォルダ構造は[Readme.md](https://github.com/pkmiya/coding-test-streamlit-todo#readme)に記述されている通りです．\
以下，ReadMeのコピーを記載します．

## フォルダ名と用途
- Backend: API サーバ
- Frontend: Web サーバ

## Backend folder structure
| 名前 | 用途 |
| ---- | ---- |
| `CRUD` | クエリ呼び出し |
| `DB` | データベース接続，モデル定義 |
| `ROUTER` | APIエンドポイント |
| `SCHEMA` | Pydantic モデル |
| `main.py` | 主となる実行ファイル |
| `requirements.txt` | pip 依存関係パッケージ |


# Preface
This web app has been created based on:
- [a web article](https://zenn.dev/tirimen/articles/7b5861c40e8a77)
- [chat-based generative AI](https://chat.openai.com/)
# Noteworthy Points
Besides, I have added the following innovations:
- QUERY INTEGRITY
  - Database model for effective and easier query calls
  - ID-based query calls for consistent data management
- READABILITY
  - Type definitions for less error-prone code
  - Consise and easy-to-read code
  - Concrete and logical ReadMe file including app explanation, folder structure, setup, and usage
- PROCESS
  - Error handling for inserting, updating, and deleting data
  - Process separation and function definition for easier debugging

# Dev outline
Basic folder structure is described at [Readme.md](https://github.com/pkmiya/coding-test-streamlit-todo#readme)\
Below is just a copy of the Readme.md file.

## Folder name and usage
- Backend: API server
- Frontend: Web server

## Backend folder structure
| Folder name | Usage |
| ---- | ---- |
| `CRUD` | SQL queries |
| `DB` | Database connection and models |
| `ROUTER` | API endpoints |
| `SCHEMA` | Pydantic models |
| `main.py` | Main file |
| `requirements.txt` | pip dependencies |